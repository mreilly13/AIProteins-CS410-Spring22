from NNModel.blackBox import load_single_data, run_NNModel
import NNModel.Util.graphs as graphs

def load(data, name, NNModel):
    dataset = load_single_data(data)
    graphs.plotData(dataset[0], name)
    return run_NNModel(NNModel, dataset)

if __name__=="__main__":
    load()