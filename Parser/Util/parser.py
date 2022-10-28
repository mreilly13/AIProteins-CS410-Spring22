# code modified from https://github.com/RosettaCommons/RFDesign/tree/main/hallucination/util/parsers.py

import numpy as np
import Parser.Util.util as util

to1letter = {
    "ALA":'A', "ARG":'R', "ASN":'N', "ASP":'D', "CYS":'C',
    "GLN":'Q', "GLU":'E', "GLY":'G', "HIS":'H', "ILE":'I',
    "LEU":'L', "LYS":'K', "MET":'M', "PHE":'F', "PRO":'P',
    "SER":'S', "THR":'T', "TRP":'W', "TYR":'Y', "VAL":'V' }

def parse_pdb(filename, **kwargs):
    '''extract xyz coords for all heavy atoms'''
    lines = open(filename,'r').readlines()
    return parse_pdb_lines(lines, **kwargs)

def parse_pdb_lines(lines):
    try:
        # indices of residues observed in the structure
        ssbond_lines = [(l) for l in lines if (l[:6]=="SSBOND")]
        for ln in range(len(lines)):
            if (lines[ln])[:6] == "ENDMDL":
                lines = lines[:ln]
                break
                
#         if l[:4]=="ATOM"):
#             #
#             atom_line = l.split(" ")
#             atom_line = [
        res = [(l[22:26],l[17:20]) for l in lines if l[:4]=="ATOM" and l[12:16].strip()=="CA"]
        
        
        seq = [util.aa2num[r[1]] if r[1] in util.aa2num.keys() else 20 for r in res]
        pdb_idx = [( l[21:22].strip(), int(l[22:26].strip()) ) for l in lines if l[:4]=="ATOM" and l[12:16].strip()=="CA"]  # chain letter, res num

        # 4 BB + up to 10 SC atoms
        xyz = np.full((len(res), 14, 3), np.nan, dtype=np.float32)
        for l in lines:
            if l[:4] != "ATOM":
                continue
            chain, resNo, atom, aa = l[21:22], int(l[22:26]), ' '+l[12:16].strip().ljust(3), l[17:20]
            idx = pdb_idx.index((chain,resNo))
            for i_atm, tgtatm in enumerate(util.aa2long[util.aa2num[aa]]):
                if tgtatm is not None and tgtatm.strip() == atom.strip(): # ignore whitespace
                    xyz[idx,i_atm,:] = [float(l[30:38]), float(l[38:46]), float(l[46:54])]
                    break

        # remove duplicated (chain, resi)
        new_idx = []
        i_unique = []
        for i,idx in enumerate(pdb_idx):
            if idx not in new_idx:
                new_idx.append(idx)
                i_unique.append(i)

        pdb_idx = new_idx
        xyz = xyz[i_unique]
        seq = np.array(seq)[i_unique]

        # parse SSBOND information
        # (serial number, chain a, sequence number a, chain b, sequence number b, bond distance)
        ssbond = []
        for i in range(len(ssbond_lines)):
            chain_a = ssbond_lines[i][14:16].strip()
            seq_num_a = int(ssbond_lines[i][17:21])
            chain_b = ssbond_lines[i][28:30].strip()
            seq_num_b = int(ssbond_lines[i][30:35])
            #distance = float(ssbond_lines[i][72:])
            #tuple = (chain_a, seq_num_a, chain_b, seq_num_b, distance)
            tuple = (chain_a, seq_num_a, chain_b, seq_num_b)
            ssbond.append(tuple)

        out = {'xyz':xyz, # cartesian coordinates [Lx14]
                'idx':[i for i in pdb_idx], # residue numbers in the PDB file [L]
                'res':[i[1] for i in res], # list of residues in the PDB file [L]
                'ssbond':ssbond # ssbond data [L]
            }
       
        print(len(out['xyz']), len(out['idx']), len(out['res']))

        return out
    
    except Exception:
        return []
