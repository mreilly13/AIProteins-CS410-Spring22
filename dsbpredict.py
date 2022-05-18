import numpy as np
import subprocess
import sys
import os
import argparse
import gzip
import shutil
import Parser.parsePDB as parser
import NNModel.init as train
import NNModel.launchModel as test
import NNModel.blackBox as model

# directories
cwd = os.getcwd()
raw_fp = "/Data/Raw/"
pdb_fp = "/Data/PDB/"
parsed_fp = "/Data/Parsed/"
rich_ss_fp = "/Data/RichSS/"
sparse_ss_fp = "/Data/SparseSS/"
no_ss_fp = "/Data/NoSS/"
graph_fp = "/Out/Graphs/"
test_fp = "/Out/Predictions/"
zip_ext = ".ent.gz"
pdb_ext = ".pdb"
parse_ext = ".csv"
result_ext = ".txt"

# parsing command line arguments
argp = argparse.ArgumentParser()
argp.add_argument("-d", "--download", action="store_true", help="check the PDB for updates, or download the PDB; zipped files are stored in Data/raw")
argp.add_argument("-a", "--all", action="store_true", help="perform entire setup process: unzip, parse, and sort the entire PDB, then train the network")
argp.add_argument("-u", "--unzip", action="store_true", help="unzip the compressed downloaded PDB files; unzipped files are stored in Data/pdb")
argp.add_argument("-p", "--parse", action="store_true", help="parse the PDB files; output files are stored in Data/parsed")
argp.add_argument("-o", "--organize", action="store_true", help="sort parsed PDB files on disulfide bonds")
argp.add_argument("-t", "--train", action="store_true", help="train the neural network")
argp.add_argument("-e", nargs='*', help="evaluate pdb files")
args = argp.parse_args()

# running
if not (args.download or args.unzip or args.parse or args.organize or args.train or args.all or args.e):
    argp.print_help()
    exit(0)
else:
    os.makedirs(os.path.dirname(cwd + raw_fp), exist_ok=True)
    os.makedirs(os.path.dirname(cwd + pdb_fp), exist_ok=True)
    os.makedirs(os.path.dirname(cwd + parsed_fp), exist_ok=True)
    os.makedirs(os.path.dirname(cwd + rich_ss_fp), exist_ok=True)
    os.makedirs(os.path.dirname(cwd + sparse_ss_fp), exist_ok=True)
    os.makedirs(os.path.dirname(cwd + no_ss_fp), exist_ok=True)
    os.makedirs(os.path.dirname(cwd + test_fp), exist_ok=True)
    
if args.download:
    proc = subprocess.Popen('/bin/bash', text=True, stdin=subprocess.PIPE, stdout=sys.stdout, stderr=sys.stderr)
    proc.communicate('Data/download.sh')
if args.unzip or args.all:
    zipped = os.listdir(cwd + raw_fp)
    zipped.sort()
    unzipped = os.listdir(cwd + pdb_fp)
    unzipped.sort()
    for pdb in zipped:
        if not pdb.endswith(zip_ext):
            continue
        name = pdb[:pdb.find(zip_ext)]
        fullname = name + pdb_ext
        raw_path = cwd + raw_fp + pdb
        pdb_path = cwd + pdb_fp + fullname
        if not (fullname in unzipped and os.path.getmtime(raw_path) < os.path.getmtime(pdb_path)):
            with gzip.open(raw_path, "rt") as infile:
                content = infile.read()
            print(name, "unzipping")
            with open(pdb_path, "w") as outfile:
                outfile.write(content)
        else:
            print(name, "up to date")
if args.parse or args.all:
    zipped = os.listdir(cwd + raw_fp)
    zipped.sort()
    unzipped = os.listdir(cwd + pdb_fp)
    unzipped.sort()
    parsed = os.listdir(cwd + parsed_fp)
    parsed.sort()
    failed_fp = cwd + "/Data/failed.csv"
    open(failed_fp, "a")
    with open(failed_fp, "r+") as f:
        failed = f.readlines()
        for pdb in unzipped:
            name = pdb[:pdb.find(pdb_ext)]
            fullname = name + parse_ext
            raw_path = cwd + raw_fp + name + zip_ext
            pdb_path = cwd + pdb_fp + pdb
            parsed_path = cwd + parsed_fp + fullname
            if not (fullname in parsed and os.path.getmtime(raw_path) < os.path.getmtime(parsed_path)) and name+'\n' not in failed:
                print(name, end=" ")
                errc, data = parser.parse(pdb_path)
                if errc == 1:
                    print("parse failed")
                    f.write(name + '\n')
                elif errc == 2:
                    print("has no CYS residues")
                    f.write(name + '\n')
                elif errc == 3:
                    print("has no bondable CYS residues")
                    f.write(name + '\n')
                else:
                    print("parse successful")
                    np.savetxt(parsed_path, data, fmt=parser.csv_format, delimiter=',')
            else:
                print(name, "already parsed")
if args.organize or args.all:
    parsed = os.listdir(cwd + parsed_fp)
    parsed.sort()
    rich_ss = os.listdir(cwd + rich_ss_fp)
    rich_ss.sort()
    sparse_ss = os.listdir(cwd + sparse_ss_fp)
    sparse_ss.sort()
    no_ss = os.listdir(cwd + no_ss_fp)
    no_ss.sort()
    for pdb in parsed:
        name = pdb[:pdb.find(parse_ext)]
        raw_path = cwd + raw_fp + name + zip_ext
        parsed_path = cwd + parsed_fp + pdb
        rich_ss_path = cwd + rich_ss_fp + pdb
        sparse_ss_path = cwd + sparse_ss_fp + pdb
        no_ss_path = cwd + no_ss_fp + pdb
        print(name, end=" ")
        if not (pdb in (rich_ss + sparse_ss + no_ss) and os.path.getmtime(raw_path) < os.path.getmtime(parsed_path)):
            pdb_data = np.loadtxt(parsed_path, dtype=parser.csv_type, delimiter=',')
            ss = 0
            nss = 0
            if pdb_data.shape == ():
                pdb_data = np.array([pdb_data])
            for line in pdb_data:
                if line[4] == 1:
                    ss += 1
                else:
                    nss += 1
            if ss == 0:
                print("has no disulfide bond")
                shutil.copyfile(parsed_path, no_ss_path)
            else:
                if 10*ss >= nss:
                    print("has high disulfide density")
                    shutil.copyfile(parsed_path, rich_ss_path)
                else:
                    print("has low disulfide density")
                    shutil.copyfile(parsed_path, sparse_ss_path)
        else:
            print("already sorted")
if args.train or args.all:
    train.main()
if args.e:
    def test_file(argpath, NNModel):
        if argpath.endswith(pdb_ext):
            name = argpath.split('/')[-1]
            name = name.removesuffix(pdb_ext)
            outpath = cwd + test_fp + name + result_ext
            errc, raw = parser.parse(argpath, False)
            if errc != 0:
                print(name, "parse failed")
            else:
                print(name, "parse succeeded")
                data = np.array([[i['dist'], i['omega'], i['theta'], i['phi'], i['ssbond'], i['chain1'], i['res1'], i['chain2'], i['res2']] for i in raw])
                results = test.load(data, NNModel, name)
                print(name, "evaluated")
                support_ss = []
                no_support_ss = []
                for i in range(len(data)):
                    if float(results[i][1]) >= .5:
                        support_ss.append(results[i])
                    else:
                        no_support_ss.append(results[i])
                support_ss.sort(key=lambda x: float(x[0]))
                no_support_ss.sort(key=lambda x: float(x[1]), reverse=True)
                with open(outpath, "w") as f:
                    f.write(f"{name}\n")
                    f.write("\nResidue pairs that may support disulfides\n")
                    f.write("res 1\tres 2\tconfidence\n\n")
                    for i in support_ss:
                        f.write(f"{i[3]} {i[4]:4}\t{i[5]} {i[6]}\t{float(i[1]):.4f}\n")
                    f.write("\nResidue pairs that may not support disulfides\n")
                    f.write("res 1\tres 2\tconfidence\n\n")
                    for i in no_support_ss:
                        f.write(f"{i[3]} {i[4]:4}\t{i[5]} {i[6]}\t{float(i[0]):.4f}\n")
        else:
            print(name, "is not a pdb file")
            
    NNModel = model.load_model("YBYF_Model_1")
    for arg in args.e:
        argpath = os.path.abspath(arg)
        if os.path.isdir(argpath):
            contents = os.listdir(argpath)
            contents.sort()
            for f in contents:
                test_file(argpath + '/' + f, NNModel)
        else:
            if os.path.exists(argpath):
                test_file(argpath, NNModel)
            else:
                print(arg, "not found")