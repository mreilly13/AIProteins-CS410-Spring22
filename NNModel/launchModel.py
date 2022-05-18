from NNModel.blackBox import load_single_data, run_NNModel
import NNModel.Util.graphs as graphs

def load(data, NNModel):
    # load data from single file
    dataset = load_single_data(data)
    # graphs.plotData(dataset[0])
    # print("LOADING IN NEURAL NETWORK MODEL")
    # NN_model = load_model("YBYF_Model_1")
    return run_NNModel(NNModel, dataset)

if __name__=="__main__":
    load()