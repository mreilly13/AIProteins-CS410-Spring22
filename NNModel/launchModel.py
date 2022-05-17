from NNModel.blackBox import load_data, load_single_data, load_ss_data, load_model, run_NNModel, run_LRModel
import NNModel.Util.graphs as graphs


def load(data):
    # load data from single file
    dataset = load_single_data(data) # put file name here
    #large_dataset = load_ss_data()
    print("LOADING IN NEURAL NETWORK MODEL")
    NN_model = load_model("YBYF_Model_1")
    return run_NNModel(NN_model, dataset)
    #regression_preped_dataset = run_NNModel(NN_model, dataset)
    # graphs.plotData(large_dataset[0])
    # print("LOADING IN REGRESSION MODEL")
    # LR_model = load_model("YBYF_Model_2")
    # return run_LRModel(LR_model, regression_preped_dataset)

if __name__=="__main__":
    load()