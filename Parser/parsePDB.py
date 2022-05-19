import numpy as np
import torch
import Parser.Util.parser as parser
import Parser.Util.geometry as geometry

# numpy values needed for .csv input/output
csv_type = [
    ('dist', np.float64), 
    ('omega', np.float64), 
    ('theta', np.float64), 
    ('phi', np.float64),
    ('ssbond', np.int32),
    ('chain1', (np.str_,1)),
    ('res1', np.int32),
    ('chain2', (np.str_,1)),
    ('res2', np.int32)
]
csv_format = ['%f','%f','%f','%f','%d','%s','%d','%s','%d']

# parse a PDB file, extracting cysteine information
def parse(filename, test=False):
    pdb = parser.parse_pdb(filename)
    if pdb == []:
        return (1 , [])
    ssbond = pdb['ssbond']
    if not test and ssbond == []:
        return (2, [])
    xyz = []
    idx = []
    res = []
    for i in range(pdb['xyz'].shape[0]):
        if test or pdb['res'][i] == "CYS":
            xyz.append(pdb['xyz'][i])
            idx.append(pdb['idx'][i])
            res.append(pdb['res'][i])
    xyz = np.array(xyz)
    xyz_ref = torch.tensor(xyz[:,:3,:]).float()
    c6d_ref = geometry.xyz_to_c6d(xyz_ref[None].permute(0,2,1,3),{'DMAX':20.0}).numpy()
    c6d = []
    i = 0
    for row in c6d_ref[0]:
        j = 0
        for col in row:
            if j > i and col[0] < 999:
                val = [n for n in col]
                if (idx[i][0], idx[i][1], idx[j][0], idx[j][1]) in ssbond:
                    val.append(1)
                else:
                    val.append(0)
                val.append(idx[i][0])
                val.append(idx[i][1])
                val.append(idx[j][0])
                val.append(idx[j][1])
                structd = np.array(tuple(val), dtype=csv_type)
                c6d.append(structd)
            j += 1
        i += 1
    return (0, c6d)