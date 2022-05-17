from NNModel.blackBox import neural_network, regression_neural_network, load_data, save_model, load_model, run_LRModel, run_NNModel, _test_load_data, load_ss_data
from NNModel.Util.helper import dataset_split, feature_scaling
import NNModel.Util.graphs as graphs


"""
Notation:
    NB = No Batch normalization
    YB = Yes Batch normalization

    NF = No Feature scaling
    YF = Yes Feature scaling
"""
def main():

    # load and split data
    # dataset = _test_load_data()
    #dataset = load_data()
    ss_dataset = load_ss_data()

    #feature_scaled_dataset = feature_scaling(dataset) # normalize the data with feature scaling formula
    feature_scaled_ss_dataset = feature_scaling(ss_dataset) # normalize the data with feature scaling formula

    #split_data = dataset_split(feature_scaled_dataset[0], feature_scaled_dataset[1])
    split_ss_data = dataset_split(feature_scaled_ss_dataset[0], feature_scaled_ss_dataset[1])

    """

        This is the model with the best results preprocessing
    """


    # 0
    #YBYF_M1 = neural_network(split_data, True, learning_rate=0.00001)
    #save_model(YBYF_M1[3], "YBYF_Model_1")

    YBYF_M2 = regression_neural_network(split_ss_data, epoch=3, layers=3, nodes=100)
    save_model(YBYF_M2, "YBYF_Model_2")


if __name__=="__main__":
    main()
