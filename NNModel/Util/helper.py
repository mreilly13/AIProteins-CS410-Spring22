import numpy as np
from tensorflow import keras
from sklearn.model_selection import train_test_split

"""

    Utility Class and Functions

"""


# helper function used to generate ROC curve and check accuracy.
def _compare_results(raw_predictions, y_test):
    y_predicted = []

    correct = 0
    total = len(raw_predictions)

    for i in range(len(raw_predictions)):
        j = np.where(raw_predictions[i,:] == max(raw_predictions[i,:]))
        #x = [0., 0., 0.] #np.zeros(3)
        x = [0., 0.]
        x[j[0][0]] = 1.
        if np.array_equal(y_test[i,:], x):
            correct += 1
        y_predicted.append(x)
    y_predicted = np.array(y_predicted)
    
    wrong = total - correct

    return [y_predicted, y_test, correct, wrong, raw_predictions]


def util_helper(y_pred, y_test):
    new_y_test = []

    for i in range(len(y_pred)):
        #if np.array_equal(y_test[i,:], np.array([1, 0, 0])):
        if np.array_equal(y_test[i,:], np.array([1, 0])):
            new_y_test.append(0)
            
        #if np.array_equal(y_test[i,:], np.array([0, 1, 0])):
        if np.array_equal(y_test[i,:], np.array([0, 1])):
            new_y_test.append(1)
            
        """
        if np.array_equal(y_test[i,:], np.array([0, 0, 1])):
            new_y_test.append(2)
        """

    return new_y_test


# normalize the dataset 
# X = (x[i] - mean) / standard_diviation
def feature_scaling(dataset):
    data = dataset[0]
    for i in range(len(data)):
        mean = np.mean(data[i, :])
        sd = np.std(data[i, :])
        data[i,:] = (data[i,:] - mean) / sd

        #mean = np.mean(data[:, i])
        #sd = np.std(data[:, i])
        #data[:,i] = (data[:,i] - mean) / sd
    
    dataset = [data, dataset[1]]
    return dataset


# split dataset
# 10% testing, 18% validation, and 72% training
def dataset_split(data, labels):
    # split the data into train, validation, and test
    x_train, x_test, y_train, y_test = train_test_split(data, labels, train_size=0.9, test_size=0.1, shuffle=True)
    x_train, x_validate, y_train, y_validate = train_test_split(x_train, y_train, train_size=0.8, test_size=0.2, shuffle=True)

    return [x_train, x_validate, x_test, y_train, y_validate, y_test]

# fix cases where only 1 of 2 classes are found
def fix_vectors(y_vector):
    h, w = y_vector.shape
    cmpr = np.ones((h, w))
    if cmpr.all() == y_vector.all():
        y_vector = np.append(y_vector, np.zeros((h, w)), axis=1)
    return y_vector


class LossAndErrorPrintingCallback(keras.callbacks.Callback):
    def __init__(self):
       self.training_batch_log = [[],[]]
       self.testing_batch_log = [[],[]]

    def returnTraining(self):
        return self.training_batch_log
    
    def returnTesting(self):
        return self.testing_batch_log

    def on_train_batch_end(self, batch, logs=None):
        #print(
        #    "Up to batch {}, the average accuracy is {:7.2f}, the average loss is {:7.2f}.".format(batch, logs["accuracy"], logs["loss"])
        #)
        self.training_batch_log[0].append(logs["accuracy"])
        self.training_batch_log[1].append(logs["loss"])

    def on_test_batch_end(self, batch, logs=None):
        #print(
        #    "Up to batch {}, the average accuracy is {:7.2f}, the average loss is {:7.2f}.".format(batch, logs["accuracy"], logs["loss"])
        #)
        self.testing_batch_log[0].append(logs["accuracy"])
        self.testing_batch_log[1].append(logs["loss"])
