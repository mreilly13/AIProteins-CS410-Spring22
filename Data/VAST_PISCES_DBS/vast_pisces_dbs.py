import sys
def db_download(filename, db):
    lines = open(filename,'r').readlines()
    data_base = []
    if(db == "VAST"): 
        for l in lines:
            l_split = l.split()
            for ids in l_split:
                data_base.append(ids[0:4])
    if(db == "PISCES"): 
        for l in lines:
            data_base.append(l[0:4])
    return data_base

def print_to_file(data_base):
    test = ",".join(data_base)
    print(test)
    
def main():
    pisces = db_download("cullpdb_pc40_res2.0_R0.25_d190801_chains15139.txt", "PISCES")
    vast = db_download("vastpe_7.txt", "VAST")
    pisces_f = open("Pisces.txt", "w")
    sys.stdout = pisces_f
    print_to_file(pisces)
    vast_f = open("Vast.txt", "w")
    sys.stdout = vast_f
    print_to_file(vast)
    sys.stdout = original_stdout
    
# if __name__ == "__main__":
main()
