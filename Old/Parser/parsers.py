import numpy as np
import scipy
import scipy.spatial
import string
import os,re
import random
import util
import numpy as np
to1letter = {
    "ALA":'A', "ARG":'R', "ASN":'N', "ASP":'D', "CYS":'C',
    "GLN":'Q', "GLU":'E', "GLY":'G', "HIS":'H', "ILE":'I',
    "LEU":'L', "LYS":'K', "MET":'M', "PHE":'F', "PRO":'P',
    "SER":'S', "THR":'T', "TRP":'W', "TYR":'Y', "VAL":'V' }

testing = 0

def parse_a3m(filename):
    '''read A3M and convert letters into integers in the 0..20 range,
    also keep track of insertions
    '''

    # read A3M file line by line
    lab,seq = [],[] # labels and sequences
    for line in open(filename, "r"):
        if line[0] == '>':
            lab.append(line.split()[0][1:])
            seq.append("")
        else:
            seq[-1] += line.rstrip()

    # parse sequences
    msa,ins = [],[]
    table = str.maketrans(dict.fromkeys(string.ascii_lowercase))
    nrow,ncol = len(seq),len(seq[0])

    for seqi in seq:

        # remove lowercase letters and append to MSA
        msa.append(seqi.translate(table))

        # 0 - match or gap; 1 - insertion
        a = np.array([0 if c.isupper() or c=='-' else 1 for c in seqi])
        i = np.zeros((ncol))

        if np.sum(a) > 0:
            # positions of insertions
            pos = np.where(a==1)[0]

            # shift by occurrence
            a = pos - np.arange(pos.shape[0])

            # position of insertions in the cleaned sequence
            # and their length
            pos,num = np.unique(a, return_counts=True)
            i[pos[pos<ncol]] = num[pos<ncol]

        # append to the matrix of insetions
        ins.append(i)

    # convert letters into numbers
    alphabet = np.array(list("ARNDCQEGHILKMFPSTWYV-"), dtype='|S1').view(np.uint8)
    msa = np.array([list(s) for s in msa], dtype='|S1').view(np.uint8)
    for i in range(alphabet.shape[0]):
        msa[msa == alphabet[i]] = i

    # treat all unknown characters as gaps
    msa[msa > 20] = 20

    ins = np.array(ins, dtype=np.uint8)

    return {"msa":msa, "labels":lab, "insertions":ins}


def parse_pdb(filename, **kwargs):
    '''extract xyz coords for all heavy atoms'''
    lines = open(filename,'r').readlines()
    return parse_pdb_lines(lines, **kwargs)

def parse_pdb_lines(lines, parse_hetatom=False, ignore_het_h=True):
    # indices of residues observed in the structure
    cys_locations = [l for l in lines if (l[:4]=="ATOM" and l[16:21].strip()=="CYS")]
    ssbond_lines = [(l) for l in lines if (l[:6]=="SSBOND")]
    res = [(l[22:26],l[17:20]) for l in lines if l[:4]=="ATOM" and l[12:16].strip()=="CA"]
    seq = [util.aa2num[r[1]] if r[1] in util.aa2num.keys() else 20 for r in res]
    pdb_idx = [( l[21:22].strip(), int(l[22:26].strip()) ) for l in lines if l[:4]=="ATOM" and l[12:16].strip()=="CA"]  # chain letter, res num
   
    # CYS Declarations
    cys_res = [(l[22:26],l[17:20]) for l in lines if l[:4]=="ATOM" and l[12:16].strip()=="CA" and l[16:21].strip()=="CYS"]
    cys_pdb_idx = [( l[21:22].strip(), int(l[22:26].strip()) ) for l in lines if l[:4]=="ATOM" and l[12:16].strip()=="CA" and l[16:21].strip()=="CYS"]  # chain letter, res num   
    no_cys_pdb_idx = [( l[21:22].strip(), int(l[22:26].strip()) ) for l in lines if l[:4]=="ATOM" and l[12:16].strip()=="CA" and l[16:21].strip()!="CYS"]  # chain letter, res num
    
    
    # 4 BB + up to 10 SC atoms
    xyz = np.full((len(res), 14, 3), np.nan, dtype=np.float32)
    index = -1
    index_check = -1
    
    cys_xyz = np.full((len(cys_res), 14, 3), np.nan, dtype=np.float32)
    cys_index = -1
    cys_index_check = -1
    
    set_a = set()
    set_b = set()
    for l in lines:
        if l[:4] != "ATOM":
            continue
        chain, resNo, atom, aa = l[21:22], int(l[22:26]), ' '+l[12:16].strip().ljust(3), l[17:20]
        idx = pdb_idx.index((chain,resNo))
        for i_atm, tgtatm in enumerate(util.aa2long[util.aa2num[aa]]):
            if tgtatm is not None and tgtatm.strip() == atom.strip(): # ignore whitespace
                xyz[idx,i_atm,:] = [float(l[30:38]), float(l[38:46]), float(l[46:54])]  
                if(l[16:21].strip()=="CYS"):
                    set_a.add(idx)
                    # CYS Check 
                    # Update index if new CYS ATOM and set XYZ of atom
                    if(cys_index_check != idx and i_atm == 0):
                        cys_index = cys_index + 1
                        cys_index_check = idx
                    cys_xyz[cys_index,i_atm,:] = xyz[idx,i_atm,:]
                    break
    
    # save atom mask
    mask = np.logical_not(np.isnan(xyz[...,0]))   
    xyz[np.isnan(xyz[...,0])] = 0.0
    cys_xyz[np.isnan(cys_xyz[...,0])] = 0.0
    
    # Create new xyz
    sorted(set_a) 
    new_xyz = np.full((len(res) - len(cys_res), 14, 3), np.nan, dtype=np.float32)
    index = 0
    for i in range(len(res)):
        if i in set_a:
            continue
        new_xyz[index,:,:] = xyz[i,:,:] 
        index = index + 1
    
    
    # remove duplicated (chain, resi)
    new_idx = []
    i_unique = []
    for i,idx in enumerate(no_cys_pdb_idx):
        if idx not in new_idx:
            new_idx.append(idx)
            i_unique.append(i)
    
    # CYS duplicated 
    cys_new_idx = []
    cys_i_unique = []
    for i,idx in enumerate(cys_pdb_idx):
        if idx not in cys_new_idx:
            cys_new_idx.append(idx)
            cys_i_unique.append(i)  
   
    # Set Unique residues 
    pdb_idx = new_idx
    xyz = new_xyz[i_unique]
    mask = mask[i_unique]
    seq = np.array(seq)[i_unique]
    cys_xyz = cys_xyz[cys_i_unique]
 
    ssbond = []
    ##ssbond manager
    #(serial number, chain a, sequence number a, chain b, sequence number b, bond distance)
    
    for i in range(len(ssbond_lines)):   
        chain_a = ssbond_lines[i][14:16].strip()
        seq_num_a = int(ssbond_lines[i][17:21])
        chain_b = ssbond_lines[i][28:30].strip()
        seq_num_b = int(ssbond_lines[i][30:35])
        distance = float(ssbond_lines[i][72:])
        tuple1 = (chain_a, seq_num_a, chain_b, seq_num_b, distance)
        ssbond.append(tuple1)
        
     
    #  Not needed for now 
    # 'mask':mask, # mask showing which atoms are present in the PDB file, [Lx14]
    # 'idx':np.array([i[1] for i in pdb_idx]), # residue numbers in the PDB file, [L]
    # 'seq':np.array(seq), # amino acid sequence, [L]
    # 'pdb_idx': pdb_idx,  # list of (chain letter, residue number) in the pdb file, [L]    
        
    out = {'xyz':xyz, # cartesian coordinates, [Lx14]  
           'cys_xyz': cys_xyz,
           'ssbonds': ssbond
           }

    # heteroatoms (ligands, etc)
    if parse_hetatom:
        xyz_het, info_het = [], []
        for l in lines:
            if l[:6]=='HETATM' and not (ignore_het_h and l[77]=='H'):
                info_het.append(dict(
                    idx=int(l[7:11]),
                    atom_id=l[12:16],
                    atom_type=l[77],
                    name=l[16:20]
                ))
                xyz_het.append([float(l[30:38]), float(l[38:46]), float(l[46:54])])

        out['xyz_het'] = np.array(xyz_het)
        out['info_het'] = info_het

    return out

def parse_fasta(filename):
    '''
    Return dict of name: seq
    '''
    out = {}
    with open(filename, 'r') as f_in:
        while True:
            name = f_in.readline().strip()[1:]
            seq = f_in.readline().strip()
            if not name: break

            out[name] = seq

    return out
