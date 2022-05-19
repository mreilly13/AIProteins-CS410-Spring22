# **DSBPredict**
Software version 1.0.0

This project was developed for and in collaboration with AIProteins: https://aiproteins.bio/#about-us

This project trains a neural network model on currently identified proteins and their structures, to predict possible residue locations that can form disulfide bonds. These possible locations for residues are ranked from most to least optimal.

<hr>

## **Contents**

- [Setup](#setup)
    - [Environment](#environment)
    - [Acquire Files](#acquire-files)
        - [Method 1: git](#method-1-git)
        - [Method 2: zip](#method-2-zip)
    - [Installation](#installation)
    - [UMB Chimera Cluster Instructions](#umb-chimera-cluster-instructions)
- [Usage](#usage)
    - [Overview](#overview)
    - [Downloading the Database](#downloading-the-database)
    - [Unzipping the Database](#unzipping-the-database)
    - [Parsing the Database](#parsing-the-database)
    - [Training the Model](#training-the-model)
    - [Perform All Preparation Functions](#perform-all-preparation-functions)
    - [Use the Model to Evaluate a Protein](#use-the-model-to-evaluate-a-protein)
    - [UMB Chimera Cluster Instructions](#umb-chimera-cluster-instructions-1)

<hr>

## **Setup**

### **Environment**

This project was developed and runs with:  
- anaconda: version 4.10.3  
- python: version 3.9.7  
- pip: version 21.2.4
- cudnn: version 8.2.1
- cudatoolkit: version 11.3.1
- setuptools: version 58.0.4
- cupy: version 10.4.0
- matplotlib: version 3.5.0
- numpy: version 1.19.5
- pandas: version 1.3.5
- scikit-learn: version 1.0.1
- scipy: version 1.7.2
- seaborn: version 0.11.2
- tensorflow: version 2.6.2
- tensorflow-gpu: version 2.6.0
- pytorch: version 1.11.0

The setup of these packages is handled by conda. If you do not already have conda installed, follow these instructions: [conda installation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

This project is designed to be run in a unix environment, on a system with a deep learning enabled NVidia GPU. The procedure to install and use may be different on other systems.

### **Acquire Files**

#### **Method 1: git**

The easiest way to acquire the files for this project is using git. In the terminal, run the command:

```
git clone https://github.com/mreilly13/DSBPredict
```

#### **Method 2: zip**

Alternatively, you can download the compressed archive [here](https://github.com/mreilly13/DSBPredict/archive/refs/heads/main.zip) and unzip it wherever you like. 

### **Installation**

All you neede to do to install this project is create the conda environment from the provided `env.yml` file. To do this, navigate to the main folder of the project and run the command:

```
conda env create -f env.yml
```

Once this finishes, run the command:

```
conda activate dsbpredict
```

### **UMB Chimera Cluster Instructions**

<details><summary>click to open</summary>
<p>

First, load the Anaconda Module by running the command:

```
$ module load anaconda3-2020.07-gcc-10.2.0-z5oxtnq
```

Restart your terminal to activate anaconda, then follow the above installation instructions.

</p>
</details>  

<hr>

## **Usage**

### **Overview**

All of the functionality of this project is managed through a single driver script, `dsbpredict`, which is called from inside the main folder of the project by running the command:

```
./dsbpredict [flags] [args]
```

The different functions are summarized by running the script with no arguments, but are explained in detail here. Most of these functions take significant time to run, so it is good practice to run this script inside of a terminal multiplexer session, like `tmux`, to allow it to run in the background. An explanation of how to use `tmux` can be found [here](https://tmuxcheatsheet.com/).

All preprocessing functions can be used to update the existing data files if there are changes, without needing to process every file; the functions automatically act only on new files.

If you do not want or need to train the neural network yourself, the repo contains a working neural network trained on the UMB Chimera Cluster: It can be used immediately following the instructions in [Use the Model to Evaluate a Protein](#use-the-model-to-evaluate-a-protein).

### **Downloading the Database**

To download the entire protein database from https://www.wwpdb.org/, run the command:

```
./dsbpredict -d
```

**WARNING:** This process takes several days, depending on the speed of your internet connection. If the process is interrupted partway through, running the same command again will resume where the previous download left off.

The database are saved in `/DSBPredict/Data/Raw/`.

### **Unzipping the Database**

To unzip the entire protein database, run the command:

```
./dsbpredict -u
```

The `.pdb` files are saved in `/DSBPredict/Data/PDB/`.

### **Parsing the Database**

This function will iterate through all the `.pdb` files, identifying cysteine pairs and performing a geometric transform to convert the cartesian coordinates of the component atoms into a relational table, computing their separation distance and relative angles. Proteins with no Disulfide bonds are ignored in this step, as they are of no use to the neural network. 

To parse the entire protein database, run the command:

```
./dsbpredict -u
```

**WARNING:** This process takes at least 12 hours, depending on the speed of your system. If the process is interrupted partway through, running the same command again will resume where the previous run left off.

The parsed data are saved as `.csv` files in `/DSBPredict/Data/Parsed/`.

### **Training the Model**

This function will use the parsed data to train a Neural Network to predict the likelihood that a pair of cysteine residues will be able to support a disulfide bond, ranking them by the network's confidence in its prediction. Further documentation of the neural network's structure is available [here]().

To train the neural network, run the command:

```
./dsbpredict -t
```

The model is saved in `/DSBPredict/NNModel/SavedModels/`. Graphs analyzing the network's training are generated in `/DSBPredict/Out/Graphs/`.

### **Perform All Preparation Functions**

To perform all above functions at once, run the command:

```
./dsbpredict -a
```

### **Use the Model to Evaluate a Protein**

To use the neural network to evaluate a `.pdb` file, run the command:

```
./dsbpredict -e [args]
```

Where `[args]` is a path to one or more `.pdb` files or directories containind `.pdb` files. This will ignore existing disulfide bonds, but will still disregard any protein without explicit cysteine residues. To force the analysis of all residue pairs, not just cysteine pairs, run the command with the additional flag:

```
./dsbpredict -e [args] --all-residues
```

This will create a report in `/DSBPredict/Out/Predictions/` for each passed protein, with the same name as the protein, but with a `.txt` extension. Residue pairs are ranked from most likely to support a disulfide bond to least likely, with a delineation at 50% confidence. This also generates a graph of the input data, in `DSBPredict/Out/Graphs/`, again with the same name as the protein, but with a `.png` extension.

### **UMB Chimera Cluster Instructions**

<details><summary>click to open</summary>
<p>

Running resource-intensive jobs on Chimera requires scheduling the job on a compute node. Chimera uses **slurm** to schedule jobs; an overview of how to use this scheduler can be found [here](https://slurm.schedmd.com/quickstart.html). An overview of the different nodes is available [here](https://www.umb.edu/rc/hpc/chimera/chimera_scheduler), or can be viewed on the cluster by running the command:

```
sinfo
```

To determine which nodes are currently in use, run the command:

```
squeue
```

To get an interactive shell on a CPU compute node, run the command:

```
$ srun -n 4 -N 1 -p [nodes] -t [duration] --pty /bin/bash  
```

where `[nodes]` is a node or comma separated list of nodes, and `[duration]` is how long you would like the session to be active for. 

Notes:
- If there is more than one node argument, slurm will choose the first available node from the list.
- This duration cannot be extended, so ensure that it is enough to complete your job. 
<hr>
To get an interactive shell on a GPU compute node, run the command:

```
$ srun -n 8 -N 1 -p DGXA100 -t [duration] --mem=30gb --gres=gpu:1 --export=NONE --pty /bin/bash
```
Once the session has been allocated, run the command:

```
$ source /etc/profile
```

At this point, use the above usage instructions.

</p>
</details>  