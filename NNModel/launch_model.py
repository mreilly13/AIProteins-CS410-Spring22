from NNModel.black_box import load_file, load_model, run_model


def main():
    # load data from single file
    dataset = load_file() # put file name here
    print("LOADING IN MODEL")
    model = load_model("Model001_510")
    regression_preped_dataset = run_model(model, dataset)


if __name__=="__main__":
    main()