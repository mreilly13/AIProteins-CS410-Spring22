# How to load the enviorment through conda 
First make sure you have anaconda installed
#### Command to Check Anaconda Versionn
```
conda --version 
```
The Anaconda Version used in cluster is 4.10.3

## Basic instruction of export and load anaconda enviorment (on windows)
https://towardsdatascience.com/how-to-export-and-load-anaconda-environments-for-data-science-projects-77dc3b781369
#### Export
```
conda env export > \Users\Dario\Desktop\environment.yml
```
#### Load
```
conda env create -f \Users\Dario\Desktop\environment.yml
```
you can change the new enviroment name at the fist line of the yaml file
```
name: tf
```

## Export windows enviorment into Linux (chimera cluster)
https://stackoverflow.com/questions/51708668/conda-environment-from-windows-to-linux
#### Export
```
conda env export --no-build > environment.yml
```
#### Load
Before load you may want to delete the last line if .yaml file is from windows OS

And the load might fail because some packages are unique to windows
just delete these missing packages until there is no error when loading

```
conda env create -f environment.yml
```
Command for activate the conda environment
```
conda activate tf
```
Command for checking the conda environment package list
```
conda list
```
Here is the list for the chimera that use to running tis project
```
(tf) [zihan.ma001@chimerahead ~]$ conda list
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
cycler                    0.11.0                   pypi_0    pypi
dataclasses               0.8                pyh6d0b6a4_7
debugpy                   1.5.1            py39h295c915_0
decorator                 5.1.1              pyhd3eb1b0_0
defusedxml                0.7.1              pyhd3eb1b0_0
dill                      0.3.4                    pypi_0    pypi
entrypoints               0.4              py39h06a4308_0
executing                 0.8.3              pyhd3eb1b0_0
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
(tf) [zihan.ma001@chimerahead ~]$
```
