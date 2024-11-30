## Anaconda 
1. Intall Anaconda3:  https://www.anaconda.com/download/success
2. Setup
``` sh
# Create env with python 3.12
conda create —name env312 python=3.12
conda activate env312
conda deactivate
conda env list

# Remove env
conda remove --name ENVIRONMENT --all

# Base env
source ~/.bashrc
# update conda end
conda update -n base -c defaults conda

# Install package
conda install -c PyTorch PyTorch
# list package
conda list
conda list --explicit
 
 # remove package
conda remove package-name
# update package
conda update PyTorch



conda install -c anaconda Jupyter
jupyter notebook

# Installation folder for anaconda at MacOS
/opt/anaconda3/envs/env312
```

## PyCharm
Setup conda type in PyCharm project
- Reference: https://docs.anaconda.com/working-with-conda/ide-tutorials/pycharm/#creating-a-new-conda-environment-from-a-pycharm-project


## VS Code
### Windows
1. Ctrl + Shift + P
2. Select Python:Select Interpreter - conda env

### MAC
1. Cmd + Shift + P
2. Select Python:Select Interpreter - conda env
