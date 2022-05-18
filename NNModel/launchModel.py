from NNModel.blackBox import load_single_data, run_NNModel

def load(data, NNModel):
    dataset = load_single_data(data)
    return run_NNModel(NNModel, dataset)

if __name__=="__main__":
    load()