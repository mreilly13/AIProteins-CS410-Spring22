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
