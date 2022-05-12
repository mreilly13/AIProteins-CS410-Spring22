from black_box import neural_network, load_data, save_model, test_load_data
from util.helper import dataset_split, feature_scaling
import util.graphs as graphs


"""
NB = No Batch normalization
YB = Yes Batch normalization

NF = No Feature scaling
YF = Yes Feature scaling

01 = learning curve of .01
25 = learning curve of .25
"""

def main():

    # load and split data
    # dataset = test_load_data()
    dataset = load_data()
    feature_scaled_dataset = feature_scaling(dataset) # normalize the data with feature scaling formula
    split_data = dataset_split(feature_scaled_dataset[0], feature_scaled_dataset[1])

    """

        This is the model with the best results preprocessing

    """

    # eta_v_loss = []
    # eta_t_loss = []

    # 0
    YBYF001 = neural_network(split_data, True, learning_rate=0.00001)
    # YBYF001 = neural_network(split_data, True, learning_rate=0.001)
    save_model(YBYF001[3], "Model001_510")
    
    # eta_v_loss.append(YBYF001[0].history['val_loss'][0])
    # eta_t_loss.append(YBYF001[0].history['loss'][0])

    # 1
    # YBYF01 = neural_network(split_data, True, learning_rate=0.01)
    # eta_v_loss.append(YBYF01[0].history['val_loss'][0])
    # eta_t_loss.append(YBYF01[0].history['loss'][0])

    # 2
    # YBYF = neural_network(split_data, True) # , batch_training=True, learning_rate = 0.000001) # With batch normalization and feature scaling
    # eta_v_loss.append(YBYF[0].history['val_loss'][0])
    # eta_t_loss.append(YBYF[0].history['loss'][0])



    """
    We probably wont be using the sigmoid activation function due to the issues it has
    """
    # 1
    sig_YBYF = neural_network(split_data, True, activation_function='sigmoid') # , batch_training=True) # With batch normalization and feature scaling using sigmoid activation function


    # Generate graphs for the best model
    graphs.roc_graph(YBYF001[2], "Model 3")
    graphs.confusion_matrix(YBYF001[2])
    graphs.multi_roc_graph(YBYF001[2], sig_YBYF[2], "ReLU Vs. Sigmoid")
    # graphs.parameter_tuning(eta_v_loss, eta_t_loss, "Different learning rate over the same model ReLU")

    # 4
    # batch_YBYF01 = neural_network(split_data, True, learning_rate=0.01, batch_training=True)


    
    # Learning curve
    # graphs.learning_curve(batch_YBYF01[4])

if __name__=="__main__":
    main()
