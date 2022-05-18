from black_box import neural_network, load_data
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
    dataset = load_data()
    split_data = dataset_split(dataset[0], dataset[1])

    # 
    v_loss = []
    t_loss = []

    # 0
    NBNF = neural_network(split_data, False) # No batch normalization and No feature scaling

    v_loss.append(NBNF[0].history['val_loss'][0])    
    t_loss.append(1)
    t_loss.append(NBNF[0].history['loss'][0])


    # 1
    YBNF = neural_network(split_data, True) # With batch normalization and No feature scaling
    v_loss.append(YBNF[0].history['val_loss'][0])
    t_loss.append(YBNF[0].history['loss'][0])



    """
    
    Models beyond this point have feature scaling enabled

    """
    feature_scaled_dataset = feature_scaling(dataset) # normalize the data with feature scaling formula                                                 # FIX
    split_data = dataset_split(feature_scaled_dataset[0], feature_scaled_dataset[1])

    # 2
    NBYF = neural_network(split_data, False) # No batch normalization and feature scaling

    graphs.roc_graph(NBYF[2], "Model 2")

    v_loss.append(NBYF[0].history['val_loss'][0])
    t_loss.append(NBYF[0].history['loss'][0])



    """

        This is the model with the best results preprocessing

    """

    eta_v_loss = []
    eta_t_loss = []

    # 3
    YBYF001 = neural_network(split_data, True, learning_rate=0.001)
    
    eta_v_loss.append(YBYF001[0].history['val_loss'][0])
    eta_t_loss.append(YBYF001[0].history['loss'][0])

    # 4
    YBYF01 = neural_network(split_data, True, learning_rate=0.01)
    eta_v_loss.append(YBYF01[0].history['val_loss'][0])
    eta_t_loss.append(YBYF01[0].history['loss'][0])

    # 5
    # ReLU
    YBYF = neural_network(split_data, True) # , batch_training=True) # With batch normalization and feature scaling
    eta_v_loss.append(YBYF[0].history['val_loss'][0])
    eta_t_loss.append(YBYF[0].history['loss'][0])



    """
    We probably wont be using the sigmoid activation function due to the issues it has
    """
    # 6
    # Sigmoid
    sig_YBYF = neural_network(split_data, True, activation_function='sigmoid') # , batch_training=True) # With batch normalization and feature scaling using sigmoid activation function


    v_loss.append(YBYF[0].history['val_loss'][0])
    t_loss.append(YBYF[0].history['loss'][0])



    """
    Note: these functions will be modified so that the graphs are saved as pdf files instead of
    havingt them displayed. 
    """
    # Generate graphs for the best model
    graphs.roc_graph(YBYF01[2], "Model 3")
    graphs.confusion_matrix(YBYF01[2])
    graphs.multi_roc_graph(YBYF01[2], sig_YBYF[2], "ReLU Vs. Sigmoid")
    
    graphs.parameter_tuning(v_loss, t_loss, "Different Preprocessing stragaties over the same model")
    graphs.parameter_tuning(eta_v_loss, eta_t_loss, "Different learning rate over the same model ReLU")

    # 7
    batch_YBYF01 = neural_network(split_data, True, learning_rate=0.01, batch_training=True)


    
    # Learning curve
    graphs.learning_curve(batch_YBYF01[4])

if __name__=="__main__":
    main()