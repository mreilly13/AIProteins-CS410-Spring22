from NNModel.black_box import load_single_data, load_model, run_model
import NNModel.util.graphs as graphs


def load(data):
    # load data from single file
    dataset = load_single_data(data) # put file name here
    print("LOADING IN MODEL")
    model = load_model("YBYF_Model_1")
    regression_preped_dataset = run_model(model, dataset)
    graphs.plotData(regression_preped_dataset[0])

if __name__=="__main__":
    load()