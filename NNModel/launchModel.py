from NNModel.blackBox import load_single_data, run_NNModel
from NNModel.Util.graphs import plot_data

def test(data, name, NNModel):
    # evaluate a single PDB with the passed model
    dataset = load_single_data(data)
    plot_data(dataset[0], name)
    return run_NNModel(NNModel, dataset)

if __name__=="__main__":
    test()