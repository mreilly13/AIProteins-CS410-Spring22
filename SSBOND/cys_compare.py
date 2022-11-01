import sys
import re


# Returns Pair ID to a PDB like format
def extract_pair_id(pair_id):
    chain_1 = pair_id[0]
    seq_1 = pair_id[1]
    check = 2
    while(pair_id[check] >= '0' and  pair_id[check] <= '9'):
        seq_1 = seq_1 + pair_id[check]
        check += 1
    seq_1 = int(seq_1)
    chain_2 = pair_id[check]
    check += 1
    seq_2 = int(pair_id[check:])
    return [chain_1, seq_1, chain_2, seq_2]

# Extracts info on given line input
def get_pair_info(line):
    line = re.split('\s+', line)
    line = list(filter(None, line))

    if(line == []):
        return False
    else:
        pair_id = line[0] + line[1] + line[2] + line[3]
        return [pair_id, float(line[4])]

# Print_results to file
def cmp_report(dsbp_dict, ssbp_dict, shared_dict, cmp_file_dir, protein_name):
    with open(cmp_file_dir + protein_name + "_r.txt", "w") as out:
        # Create Header
        out.write("Res 1    Res 2    Confidence    Difference\nShared Bonds\n")
        # Shared
        sorting = sorted(shared_dict.items(), key=lambda item: max(item[1]))
        for i in range(len(sorting)):
            ex = extract_pair_id(sorting[i][0])
            txt = "{res_1}  {seq_1}    {res_2}  {seq_2}  {conf_1}, {conf_2} {diff}\n".format(res_1 = ex[0], seq_1 = ex[1], res_2 = ex[2], seq_2 = ex[3],
                                                                                             conf_1 = max(sorting[i][1]), conf_2 = min(sorting[i][1]),
                                                                                             diff = round((sorting[i][1][0] - sorting[i][1][1]), 6))
            out.write(txt)
        out.write("\n\nDSBPredict results\n")
        # DSBPredict
        sorting = sorted(dsbp_dict.items(), key=lambda item: item[1])
        for i in range(len(sorting) - 1, -1, -1):
            ex = extract_pair_id(sorting[i][0])
            txt = "{res_1}  {seq_1}    {res_2}  {seq_2}  {conf_1}\n".format(res_1 = ex[0], seq_1 = ex[1],
                                                                            res_2 = ex[2], seq_2 = ex[3],
                                                                            conf_1 = sorting[i][1])
            out.write(txt)
        out.write("\n\nSSBondPredict results\n")
        # SSBONDPredict
        sorting = sorted(ssbp_dict.items(), key=lambda item: item[1])
        for i in range(len(sorting) - 1, -1, -1):
            ex = extract_pair_id(sorting[i][0])
            txt = "{res_1}  {seq_1}    {res_2}  {seq_2}  {conf_1}\n".format(res_1 = ex[0], seq_1 = ex[1],
                                                                            res_2 = ex[2], seq_2 = ex[3],
                                                                            conf_1 = sorting[i][1])
            out.write(txt)
        out.close()

def compare(DSBP_file, SSBP_file, cmp_file_dir):

    shared_dict = {}
    dsbp_dict = {}
    ssbp_dict = {}
    dsbp = open(DSBP_file, "r")
    protein_name = dsbp.readline()
    for i in range(3): dsbp.readline() # Ignore Header
    read = dsbp.readline()

    # Put DSBP output into dictionary
    while(read != [] or read != 'EOF'):
        if(read == '\n'):
            read = dsbp.readline()
            continue
        info = get_pair_info(read)
        if (info == False): break
        dsbp_dict[info[0]] = info[1]
        read = dsbp.readline()
    dsbp.close()

    # Add SSBP output into dictionary
    # Find the results from SSBond predict in dictionary
    # if in dictionary append result and update file status
    # else add to dict
    ssbp = open(SSBP_file, "r")
    ssbp.readline() # Ignore Header
    read = ssbp.readline()
    while(read != [] or read != 'EOF'):
        info = get_pair_info(read)
        if (info == False): break
        # Check if a pair found in SSBondPredict also exists DSBPredict
        if(info[0] in dsbp_dict):
            # Add entry to common dict
            li = [dsbp_dict[info[0]]]
            li.append(info[1])
            shared_dict[info[0]] = li
            # Remove entry in dsbp
            del dsbp_dict[info[0]]
        else:
            ssbp_dict[info[0]] = info[1]
        read = ssbp.readline()
    ssbp.close()
    cmp_report(dsbp_dict, ssbp_dict, shared_dict, cmp_file_dir, protein_name)

# python3 cys_compare.py dsbp_out ssbp_out report_dir

def main():
    DSBP_file = sys.argv[1]  # DSBPredict output file
    SSBP_file = sys.argv[2]  # SSBondPredict output file
    cmp_file_dir = sys.argv[3] # Location to store new file
    compare(DSBP_file, SSBP_file, cmp_file_dir)

if __name__=="__main__":
    main()