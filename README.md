# AI Proteins
Software version 1.0.0  

## List of contents
* [General info](#general-info)  
* [Running required modules](#running-required-modules)  
* [Setup](#setup)   
* [UMB Chimera script](#umb-chimera-script)  
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

#### Here is the list from the chimera that use to running tis project:(not all of them are needed)
check the list under conda envirment 
```
$ conda list
```
<details><summary>click to open</summary>
<p>
        
```
# packages in environment at /home/zihan.ma001/.conda/envs/tf:
#
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main  
_openmp_mutex             4.5                       1_gnu  
_tflow_select             2.1.0                       gpu  
abseil-cpp                20210324.2           h2531618_0  
absl-py                   0.13.0           py39h06a4308_0  
aiohttp                   3.8.1            py39h7f8727e_1  
aiosignal                 1.2.0              pyhd3eb1b0_0  
anyio                     3.5.0            py39h06a4308_0  
argon2-cffi               21.3.0             pyhd3eb1b0_0  
argon2-cffi-bindings      21.2.0           py39h7f8727e_0  
astor                     0.8.1            py39h06a4308_0  
asttokens                 2.0.5              pyhd3eb1b0_0  
astunparse                1.6.3                      py_0  
async-timeout             4.0.1              pyhd3eb1b0_0  
attrs                     21.2.0             pyhd3eb1b0_0  
babel                     2.9.1              pyhd3eb1b0_0  
backcall                  0.2.0              pyhd3eb1b0_0  
beautifulsoup4            4.11.1           py39h06a4308_0  
blas                      1.0                         mkl  
bleach                    4.1.0              pyhd3eb1b0_0  
blinker                   1.4              py39h06a4308_0  
brotlipy                  0.7.0           py39h27cfd23_1003  
c-ares                    1.18.1               h7f8727e_0  
ca-certificates           2022.3.29            h06a4308_1  
cachetools                4.2.2              pyhd3eb1b0_0  
certifi                   2021.10.8        py39h06a4308_2  
cffi                      1.15.0           py39hd667e15_1  
charset-normalizer        2.0.4              pyhd3eb1b0_0  
clang                     5.0                      pypi_0    pypi
click                     8.0.3              pyhd3eb1b0_0  
colorama                  0.4.4              pyhd3eb1b0_0  
cryptography              3.4.8            py39hd23ed53_0  
cudatoolkit               11.3.1               h2bc3f7f_2  
cudnn                     8.2.1                cuda11.3_0  
cupy-cuda113              10.4.0                   pypi_0    pypi
cycler                    0.11.0                   pypi_0    pypi
dataclasses               0.8                pyh6d0b6a4_7  
debugpy                   1.5.1            py39h295c915_0  
decorator                 5.1.1              pyhd3eb1b0_0  
defusedxml                0.7.1              pyhd3eb1b0_0  
dill                      0.3.4                    pypi_0    pypi
entrypoints               0.4              py39h06a4308_0  
executing                 0.8.3              pyhd3eb1b0_0  
fastrlock                 0.8                      pypi_0    pypi
flatbuffers               1.12                     pypi_0    pypi
fonttools                 4.28.3                   pypi_0    pypi
frozenlist                1.2.0            py39h7f8727e_0  
gast                      0.4.0              pyhd3eb1b0_0  
giflib                    5.2.1                h7b6447c_0  
google-auth               1.33.0             pyhd3eb1b0_0  
google-auth-oauthlib      0.4.1                      py_2  
google-pasta              0.2.0              pyhd3eb1b0_0  
googleapis-common-protos  1.56.0                   pypi_0    pypi
grpcio                    1.42.0           py39hce63b2e_0  
h5py                      3.1.0                    pypi_0    pypi
hdf5                      1.10.6               hb1b8bf9_0  
icu                       68.1                 h2531618_0  
idna                      3.3                pyhd3eb1b0_0  
importlib-metadata        4.8.2            py39h06a4308_0  
intel-openmp              2021.4.0          h06a4308_3561  
ipykernel                 6.9.1            py39h06a4308_0  
ipython                   8.2.0            py39h06a4308_0  
ipython_genutils          0.2.0              pyhd3eb1b0_1  
jedi                      0.18.1           py39h06a4308_1  
jinja2                    3.0.3              pyhd3eb1b0_0  
joblib                    1.1.0                    pypi_0    pypi
jpeg                      9d                   h7f8727e_0  
json5                     0.9.6              pyhd3eb1b0_0  
jsonschema                4.4.0            py39h06a4308_0  
jupyter-http-over-ws      0.0.8                    pypi_0    pypi
jupyter_client            7.2.2            py39h06a4308_0  
jupyter_core              4.9.2            py39h06a4308_0  
jupyter_server            1.13.5             pyhd3eb1b0_0  
jupyterlab                3.3.2              pyhd3eb1b0_0  
jupyterlab_pygments       0.1.2                      py_0  
jupyterlab_server         2.12.0           py39h06a4308_0  
keras                     2.6.0                    pypi_0    pypi
keras-preprocessing       1.1.2              pyhd3eb1b0_0  
kiwisolver                1.3.2                    pypi_0    pypi
krb5                      1.19.2               hac12032_0  
ld_impl_linux-64          2.35.1               h7274673_9  
libcurl                   7.78.0               h0b77cf5_0  
libedit                   3.1.20210910         h7f8727e_0  
libev                     4.33                 h7f8727e_1  
libffi                    3.3                  he6710b0_2  
libgcc-ng                 9.3.0               h5101ec6_17  
libgfortran-ng            7.5.0               ha8ba4b0_17  
libgfortran4              7.5.0               ha8ba4b0_17  
libgomp                   9.3.0               h5101ec6_17  
libnghttp2                1.46.0               hce63b2e_0  
libpng                    1.6.37               hbc83047_0  
libprotobuf               3.14.0               h8c45485_0  
libsodium                 1.0.18               h7b6447c_0  
libssh2                   1.9.0                h1ba5d50_1  
libstdcxx-ng              9.3.0               hd4cf53a_17  
llvmlite                  0.37.0                   pypi_0    pypi
markdown                  3.3.4            py39h06a4308_0  
markupsafe                2.0.1            py39h27cfd23_0  
matplotlib                3.5.0                    pypi_0    pypi
matplotlib-inline         0.1.2              pyhd3eb1b0_2  
mistune                   0.8.4           py39h27cfd23_1000  
mkl                       2021.4.0           h06a4308_640  
mkl-service               2.4.0            py39h7f8727e_0  
mkl_fft                   1.3.1            py39hd3c417c_0  
mkl_random                1.2.2            py39h51133e4_0  
multidict                 5.1.0            py39h27cfd23_2  
nbclassic                 0.3.5              pyhd3eb1b0_0  
nbclient                  0.5.13           py39h06a4308_0  
nbconvert                 6.4.4            py39h06a4308_0  
nbformat                  5.3.0            py39h06a4308_0  
ncurses                   6.3                  h7f8727e_2  
nest-asyncio              1.5.5            py39h06a4308_0  
notebook                  6.4.8            py39h06a4308_0  
numba                     0.54.1                   pypi_0    pypi
numpy                     1.19.5                   pypi_0    pypi
oauthlib                  3.1.1              pyhd3eb1b0_0  
opencv-python             4.5.4.60                 pypi_0    pypi
openssl                   1.1.1n               h7f8727e_0  
opt_einsum                3.3.0              pyhd3eb1b0_1  
packaging                 21.3               pyhd3eb1b0_0  
pandas                    1.3.5                    pypi_0    pypi
pandocfilters             1.5.0              pyhd3eb1b0_0  
parso                     0.8.3              pyhd3eb1b0_0  
pexpect                   4.8.0              pyhd3eb1b0_3  
pickleshare               0.7.5           pyhd3eb1b0_1003  
pillow                    8.4.0                    pypi_0    pypi
pip                       21.2.4           py39h06a4308_0  
prometheus_client         0.13.1             pyhd3eb1b0_0  
promise                   2.3                      pypi_0    pypi
prompt-toolkit            3.0.20             pyhd3eb1b0_0  
protobuf                  3.14.0           py39h2531618_1  
ptyprocess                0.7.0              pyhd3eb1b0_2  
pure_eval                 0.2.2              pyhd3eb1b0_0  
pyasn1                    0.4.8              pyhd3eb1b0_0  
pyasn1-modules            0.2.8                      py_0  
pycparser                 2.21               pyhd3eb1b0_0  
pygments                  2.11.2             pyhd3eb1b0_0  
pyjwt                     2.1.0            py39h06a4308_0  
pyopenssl                 21.0.0             pyhd3eb1b0_1  
pyparsing                 3.0.6                    pypi_0    pypi
pyrsistent                0.18.0           py39heee7806_0  
pysocks                   1.7.1            py39h06a4308_0  
python                    3.9.7                h12debd9_1  
python-dateutil           2.8.2              pyhd3eb1b0_0  
python-fastjsonschema     2.15.1             pyhd3eb1b0_0  
pytz                      2021.3             pyhd3eb1b0_0  
pyyaml                    6.0                      pypi_0    pypi
pyzmq                     22.3.0           py39h295c915_2  
readline                  8.1.2                h7f8727e_1  
requests                  2.26.0             pyhd3eb1b0_0  
requests-oauthlib         1.3.0                      py_0  
rsa                       4.7.2              pyhd3eb1b0_1  
scikit-learn              1.0.1                    pypi_0    pypi
scipy                     1.7.1            py39h292c36d_2  
seaborn                   0.11.2                   pypi_0    pypi
send2trash                1.8.0              pyhd3eb1b0_1  
setuptools                58.0.4           py39h06a4308_0  
setuptools-scm            6.3.2                    pypi_0    pypi
six                       1.15.0                   pypi_0    pypi
snappy                    1.1.8                he6710b0_0  
sniffio                   1.2.0            py39h06a4308_1  
soupsieve                 2.3.1              pyhd3eb1b0_0  
sqlite                    3.36.0               hc218d9a_0  
stack_data                0.2.0              pyhd3eb1b0_0  
tensorboard               2.6.0                    pypi_0    pypi
tensorboard-data-server   0.6.1                    pypi_0    pypi
tensorboard-plugin-wit    1.6.0                      py_0  
tensorflow                2.6.2                    pypi_0    pypi
tensorflow-datasets       4.5.2                    pypi_0    pypi
tensorflow-estimator      2.6.0                    pypi_0    pypi
tensorflow-gpu            2.6.0                    pypi_0    pypi
tensorflow-metadata       1.7.0                    pypi_0    pypi
termcolor                 1.1.0            py39h06a4308_1  
terminado                 0.13.1           py39h06a4308_0  
testpath                  0.5.0              pyhd3eb1b0_0  
threadpoolctl             3.0.0                    pypi_0    pypi
tk                        8.6.11               h1ccaba5_0  
tomli                     1.2.2                    pypi_0    pypi
torch                     1.11.0                   pypi_0    pypi
tornado                   6.1              py39h27cfd23_0  
tqdm                      4.64.0                   pypi_0    pypi
traitlets                 5.1.1              pyhd3eb1b0_0  
typing-extensions         3.7.4.3                  pypi_0    pypi
tzdata                    2021e                hda174b7_0  
urllib3                   1.26.7             pyhd3eb1b0_0  
wcwidth                   0.2.5              pyhd3eb1b0_0  
webencodings              0.5.1            py39h06a4308_1  
websocket-client          0.58.0           py39h06a4308_4  
werkzeug                  2.0.2              pyhd3eb1b0_0  
wheel                     0.35.1             pyhd3eb1b0_0  
wrapt                     1.12.1                   pypi_0    pypi
xz                        5.2.5                h7f8727e_1  
yarl                      1.6.3            py39h27cfd23_0  
zeromq                    4.3.4                h2531618_0  
zipp                      3.6.0              pyhd3eb1b0_0  
zlib                      1.2.11               h7f8727e_4  
        
```
        
</p>
</details>

## Setup  

### 1. Git command for moving project into cluster

<details><summary>click to open</summary>
<p>

#### Make a copy (At the first time)
```
$ git clone
```
#### Get changes (It the projec already exist)
Do under the path /DSBPredict/
```
$ git stash
```
then
```
$ git pull
```

</p>
</details>       

### 2. Install(Load) Anaconda on UMB chimera cluster

<details><summary>click to open</summary>
<p>

#### Load Anaconda on UMB chimera cluster
first, find Anaconda version that avaliable on chimera cluster module
```
$ module show
```
then, load needed Anaconda version (in this case, Anaconda verson >= 4.10.3)
```
$ module load
```
Filally, check all loaded modules
```
$ module list
```
Remenber you need to restart the terminal after first load Anaconda

Official instructions on module: https://www.umb.edu/rc/kb/modules

</p>
</details>       

### 3. Load einvirment into cluster
detiled infomation is in Environment folder

<details><summary>click to open</summary>
<p>

#### First change path to /DSBPredict/environment/
```
$ cd /DSBPredict/environment/
```
#### Command for load the environment (use under the conda envirment) 
```
$ conda env create -f environment.yml
```

</p>
</details>       

### 4. PyTorch  (now this and scipy are just for record the fomat since conda command should set up everything)

<details><summary>click to open</summary>
<p>

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

</p>
</details>       

## UMB Chimera script  

#### Allocate resource on chimera  

Try a different partition or specify multiple partitions (comma separated list) to allow it to use any partition on the list you give it.  

List for the cores: https://www.umb.edu/rc/hpc/chimera/chimera_scheduler  
Or use 'sinfo' to check the list of cores
```
$ sinfo
```
#### Run projct on CPU nodes
```
$ srun -n 4 -N 1 -p Intel6126,Intel6240,AMD6276 -t 01:00:00 --pty /bin/bash  
```
This will find first avaliable node in Intel6126, Intel6240 and AMD6276.
#### Run projct on GPU nodes
```
$ srun -n 8 -N 1 -p DGXA100 -t 01:00:00 --mem=40gb --gres=gpu:1 --export=NONE --pty /bin/bash
```
When submitting to the  GPU nodes: need to add "--gres=gpu:1 --export=NONE"  to the command,  and after login need to issue command "source /etc/profile".
```
$ source /etc/profile
```

#### Check the current waiting list  
```
$ squeue  
```












