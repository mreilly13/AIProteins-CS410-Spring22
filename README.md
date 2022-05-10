# AI Proteins
Software version 1.0.0  

## List of contents
* [General info](#general-info)  
* [Running required modules](#running-required-modules)  
* [Setup](#setup)   
* [Chimera script](#chimera-script)  
* [xxx](#xxx)  

## General info  

AIProteins is a biotechnology startup working on developing new proteins. AIProteins is focused on designing and engineering miniproteins for therapeutic and medical uses. An integral amino acid to design new proteins is cysteine. This amino acid is unique because of its natural ability to form bonds reversible covalent bonds in proteins. One of the important things in creating new proteins is to identify locations where cysteine can form stable disulfide(S-S) bonds. In this project we train a neural network model on currently identified proteins and their structures, so when working with new proteins the model can predict possible residue locations that can form disulfide bonds. These possible locations for residues are ranked from most to least optimal.
## Running required modules  

This project is created and run with:  
Anaconda verson == 4.10.3  
Python verson == 3.9.7  
Jupyter Notebook == xxx  
xxx verson == xxx  
xxx verson == xxx  

## Setup  

1. PyTorch  
#### Install PyTorch using pip  
We can install the PyTorch by using pip command; run the following command in the terminal:
```
pip3 install torch torchvision torchaudio  
```
#### Install PyTorch using Anaconda  
We can also install PyTorch by using Anaconda. First, we need to download the Anaconda navigator and then open the anaconda prompt type the following command:
```
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch  
```

#### Verification
To ensure that PyTorch was installed correctly, we can verify the installation by running sample PyTorch code. Here we will construct a randomly initialized tensor.  

From the command line, type:  
```
python
```
then enter the following code:
```
import torch
x = torch.rand(5, 3)
print(x)
```
The output should be something similar to:
```
tensor([[0.3380, 0.3845, 0.3217],
        [0.8337, 0.9050, 0.2650],
        [0.2979, 0.7141, 0.9069],
        [0.1449, 0.1132, 0.1375],
        [0.4675, 0.3947, 0.1426]])
```
Additionally, to check if your GPU driver and CUDA is enabled and accessible by PyTorch, run the following commands to return whether or not the CUDA driver is enabled:
```
import torch
torch.cuda.is_available()
```
2. SciPy
#### Install SciPy using pip  
We can install the SciPy library by using pip command; run the following command in the terminal:
```
pip install scipy  
```
#### Install SciPy using Anaconda  
We can also install SciPy packages by using Anaconda. First, we need to download the Anaconda navigator and then open the anaconda prompt type the following command:
```
conda install -c anaconda scipy  
```


## Chimera script  

#### Allocate resource on chimera  

Try a different partition or specify multiple partitions (comma separated list) to allow it to use any partition on the list you give it.  

List for the cores: https://www.umb.edu/rc/hpc/chimera/chimera_scheduler  
```
$ srun -n 4 -N 1 -p Intel6126,Intel6240,AMD6276 -t 01:00:00 --pty /bin/bash  
```
#### Check the current waiting list  
```
$ squeue  
```
#### Help info  
```
$ sinfo  
```











