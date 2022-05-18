import os
import numpy as np
import cupy as cp
from tensorflow import keras
from tensorflow.keras import utils
from tensorflow.keras.layers import BatchNormalization, Dense, Dropout
from tensorflow.keras.models import Sequential
from NNModel.Util.helper import LossAndErrorPrintingCallback, _compare_results, fix_vectors

def load_data():
    #Load preparsed data - GPU accelerated version

    cwd = os.getcwd()
    rich_ss_fp = "/Data/RichSS/"
    rich_ss = os.listdir(cwd + rich_ss_fp)
    rich_ss.sort()
    
    data = cp.zeros((1, 9))

    for i in rich_ss:
        pdb_data = cp.genfromtxt(cwd + rich_ss_fp + i, delimiter=",")
        if pdb_data.shape == (9,):
            pdb_data = cp.array([pdb_data])
        data = cp.append(data,pdb_data,axis=0)
    
    data = data[1:]

    features = cp.copy(data[:, 0:4])
    
    # preprocessing
    features[:, 0] = features[:, 0] / 20.0
    features[:, 1] = features[:, 1] / cp.pi
    features[:, 2] = features[:, 2] / cp.pi
    features[:, 3] = features[:, 3] / cp.pi
    labels = cp.copy(data[:, 4])

    return [features.get(), labels.get()]
    
"""
def load_data():
    # Load preparsed data - CPU version

    cwd = os.getcwd()
    rich_ss_fp = "/Data/RichSS/"
    rich_ss = os.listdir(cwd + rich_ss_fp)
    rich_ss.sort()
    
    data = np.zeros((1, 9))

    for i in rich_ss:
        pdb_data = np.genfromtxt(cwd + rich_ss_fp + i, delimiter=",")
        if pdb_data.shape == (9,):
            pdb_data = np.array([pdb_data])
        data = np.append(data,pdb_data,axis=0)
    
    data = data[1:]

    features = np.copy(data[:, 0:4])
    
    # preprocessing
    features[:, 0] = features[:, 0] / 20.0
    features[:, 1] = features[:, 1] / np.pi
    features[:, 2] = features[:, 2] / np.pi
    features[:, 3] = features[:, 3] / np.pi
    
    labels = np.copy(data[:, 4])

    return [features, labels]
"""

# meant to be used when testing a loaded model.
def load_single_data(_data):
    """ load individual file data """

    data = _data
    features = np.copy(data[:, 0:4]).astype(np.float32)
    
    # preprocessing
    features[:, 0] = features[:, 0] / 20.0
    features[:, 1] = features[:, 1] / np.pi
    features[:, 2] = features[:, 2] / np.pi
    features[:, 3] = features[:, 3] / np.pi

    labels = np.copy(data[:, 4:])

    return [features, labels]

def load_ss_data():
    data = load_data()
    features = data[0]
    labels = data[1]

    ss_features = []
    non_ss_features = []

    for i in range(len(features)):
        if labels[i] == 1:
            ss_features.append(features[i])
        else:
            non_ss_features.append(features[i])
    ss_features = np.array(ss_features)
    ss_labels = np.ones((len(ss_features)))
    non_ss_features = np.array(non_ss_features)
    non_ss_labels = np.zeros((len(non_ss_features)))

    noise_ratio = .02
    noise = int(len(non_ss_features) * noise_ratio)

    noise_features = non_ss_features[:noise, :]
    noise_labels = non_ss_labels[:noise]

    features = np.append(ss_features, noise_features, axis= 0)
    labels = np.append(ss_labels, noise_labels, axis= 0)
    
    return [features, labels]

def neural_network(data, batchNormalize=True, learning_rate=0.00001, batch_training=False, activation_function='ReLU'):
    """ Neural Network Model """

    # load the data in.
    x_train = data[0]
    x_validate = data[1]
    x_test = data[2]

    y_train = data[3]
    y_validate = data[4]
    y_test = data[5]

    # Hyperparameters:
    num_epochs = 20 # 20
    batch_size = 100 # 75
    
    if batch_training:
        num_epochs = 1
        batch_size = 1

    eta = learning_rate
    decay_factor = 0.95
    size_hidden = 300 # 300

    # static parameters
    size_input = 4 # number of features
    size_output =  2 # number of labels
    Input_shape = (size_input,)

    # Neural Network Model
    _model = []
    _model.append(keras.Input(shape=Input_shape, name='input_layer'))
    _model.append(Dense(size_hidden, activation=activation_function, name='hidden_layer01'))
    
    if batchNormalize:
        _model.append(BatchNormalization())
    
    _model.append(Dense(size_hidden, activation=activation_function, name='hidden_layer02'))
    _model.append(Dropout(.05))
    _model.append(Dense(size_hidden, activation=activation_function, name='hidden_layer03'))
    
    if batchNormalize:
        _model.append(BatchNormalization())
    
    _model.append(Dense(size_hidden, activation=activation_function, name='hidden_layer04'))
    _model.append(Dropout(.05))
    _model.append(Dense(size_hidden, activation=activation_function, name='hidden_layer05'))
    
    if batchNormalize:
        _model.append(BatchNormalization())

    _model.append(Dense(size_hidden, activation=activation_function, name='hidden_layer06'))
    _model.append(Dense(size_hidden, activation=activation_function, name='hidden_layer07'))
    _model.append(Dense(size_output, activation='softmax', name='output_layer'))

    model = Sequential(_model)

    # Model information
    model.summary()

    # initializing label in vector form [1, 0, ...], [0, 1, ...], ...
    y_train_vectors = keras.utils.to_categorical(y_train)
    y_test_vectors = keras.utils.to_categorical(y_test)
    y_validate_vectors = keras.utils.to_categorical(y_validate)

    y_train_vectors = fix_vectors(y_train_vectors)
    y_test_vectors = fix_vectors(y_test_vectors)
    y_validate_vectors = fix_vectors(y_validate_vectors)

    # setting up optimizer and scheduler
    learning_rate_schedule = keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=eta, decay_steps=x_train.shape[0], decay_rate=decay_factor)

    optimizer = keras.optimizers.Adam(learning_rate=learning_rate_schedule)
                #keras.optimizers.Adamax(learning_rate=learning_rate_schedule)
                #keras.optimizers.Adagrad(learning_rate=learning_rate_schedule) 
                #keras.optimizers.SGD(learning_rate=learning_rate_schedule)
    
    loss_function = keras.losses.categorical_crossentropy

    # setting up model.
    model.compile(loss=loss_function, optimizer=optimizer, metrics='accuracy')

    if batch_training: # we are training with a epoch of 1 and batch_size of 1 to obtain the learning curve.
        _batch_learning_curve_info = LossAndErrorPrintingCallback()
        
        # history.history['accuracy']['val_accuracy']['loss']['val_loss']
        _history = model.fit(x_train, y_train_vectors, batch_size=batch_size, epochs=num_epochs, validation_data=(x_validate, y_validate_vectors), verbose=2, callbacks=[_batch_learning_curve_info])
    else:
        _history = model.fit(x_train, y_train_vectors, batch_size=batch_size, epochs=num_epochs, validation_data=(x_validate, y_validate_vectors), verbose=2)

    # [loss, accuracy]
    results = model.evaluate(x_test, y_test_vectors, batch_size)

    # prediction
    predictions = model.predict(x_test)

    # Return this
    _prediction_info = _compare_results(predictions, y_test_vectors)
    
    correct = _prediction_info[2]
    wrong = _prediction_info[3]
    total = correct + wrong
    print(f"Total:{total}, Correct: {correct}, Incorrect: {wrong}")

    # fit, evaluation, prediction
    if batch_training:
        return [_history, results, _prediction_info, _batch_learning_curve_info.returnTraining(), _batch_learning_curve_info.returnTesting(), model]
    
    return [_history, results, _prediction_info, model]

def run_NNModel(model, data):
    features = data[0]
    labels_raw = data[1]
    labels = labels_raw[:, 0].astype(np.float32)
    y_vectors = utils.to_categorical(labels)
    y_vectors = fix_vectors(y_vectors)
    predictions = model.predict(features)
    _prediction_info = _compare_results(predictions, y_vectors)
    y_predicted = _prediction_info[4]
    return np.append(y_predicted, labels_raw, axis = 1)

def save_model(model, fileName):
    cwd = os.getcwd()
    sm_path = "/NNModel/SavedModels/"
    os.makedirs(os.path.dirname(cwd + sm_path), exist_ok=True)
    model.save(cwd + sm_path + fileName)

def load_model(fileName):
    cwd = os.getcwd()
    sm_path = "/NNModel/SavedModels/"
    model = keras.models.load_model(cwd + sm_path + fileName)
    model.summary()
    return model