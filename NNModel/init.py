from NNModel.blackBox import neural_network, save_model, load_ss_data
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
    print("LOADING DATA")
    ss_dataset = load_ss_data()
    print("PREPROCESSING DATA")
    feature_scaled_ss_dataset = feature_scaling(ss_dataset)
    split_ss_data = dataset_split(feature_scaled_ss_dataset[0], feature_scaled_ss_dataset[1])
    YBYF_M1 = neural_network(split_ss_data, True, learning_rate=0.00001)
    save_model(YBYF_M1[3], "YBYF_Model_1")
    print("MODEL SAVED")

if __name__=="__main__":
    main()
