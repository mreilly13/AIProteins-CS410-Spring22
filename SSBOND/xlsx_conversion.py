import csv
import pandas as pd
import sys

# Generates both a txt and csv file of the SSBONDPredict output
def SSBONDPredict_Converter(txt_dir, xlxs_dir, csv_dir, name):
    # Extract keys
    dfs = pd.read_excel(xlxs_dir, sheet_name="probability")
    probabilities = dfs["probability"]
    indexes = dfs["Unnamed: 0"]
    keys = dfs["key"][0][12:-2]
    keys = keys.split(", ")
    # Extract and reorganize xlxs data
    data = {}
    for i in range(len(indexes)):
        # Residue 1
        key = keys[indexes[i]].replace(" ", "")
        key = key.split("-")
        res_1 = key[0][1:4]
        chain_1 = key[0][4]
        seq_1 = int(key[0][5:])
        # Residue 2
        res_2 = key[1][0:3]
        chain_2 = key[1][3]
        seq_2 = int(key[1][4:-1])
        if(res_1 == "CYS" and res_2 == "CYS"):
            #IDs
            pair_id = res_1 + str(seq_1) + res_2 + str(seq_2)
            reverse_id = res_2 + str(seq_2) + res_1 + str(seq_1)
            # check for vice-versa pairs and remove the smaller confidence id from the data
            if (reverse_id in data):
                if(data[reverse_id][6] <  probabilities[indexes[i]]):
                    # Labels: [residue 1, chain 1, seq 1, residue 2, chain 2, seq 2, probability]
                    del data[reverse_id]
                else:
                    continue
            data[pair_id] = [res_1, chain_1, seq_1, res_2, chain_2, seq_2, probabilities[indexes[i]]]
        else:
            continue

    data = sorted(data.values(), key = lambda values: values[6], reverse = True)

    # Create csv file
    header = ['Res 1', '', '', 'Res 2', ' ', '', ' Confidence']
    with open(csv_dir, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)

    # Create txt file
    with open(txt_dir, "w") as my_output_file:
        my_output_file.write(f"{name}\n")
        my_output_file.write("\nres 1  res 2  confidence\n\n")
        for i in range(len(data)):
            # txt = "{chain_1}{between}{seq_1}{between}{chain_2}{between}{seq_2}{between}{between}{conf}\n".format(res_1 = data[i][0], chain_1 = data[i][1],
            #                                                                                                      seq_1 = data[i][2], res_2 = data[i][3],
            #                                                                                                      chain_2 = data[i][4], between = ' '*2,
            #                                                                                                      seq_2 = data[i][5], conf = data[i][6])
            # my_output_file.write(txt)
            my_output_file.write(f"{data[i][1]} {data[i][2]:<4} {data[i][4]} {data[i][5]:<4} {data[i][6]:.3f}\n")
        my_output_file.close()

# Directory of xlxs directory and name of xlxs file (must include .xlss in CLA) as input
# e.g. python3 xlxs_conversion.py ~/data/pdb/ pdb1.xlsx
# Translates and creates csv and txt files of xlxs and stores in same directory
def main():
    directory = sys.argv[1]
    xlxs_dir = directory + sys.argv[2]
    name = sys.argv[2].split(".")
    txt_dir = directory + name[0] + ".txt"
    csv_dir = directory + name[0] + ".csv"
    SSBONDPredict_Converter(txt_dir, xlxs_dir, csv_dir, name[0])

if __name__=="__main__":
    main()
