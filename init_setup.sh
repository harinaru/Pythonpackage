#clear
echo [$(date)]: "START"
echo [$(date)]: "Creating a conda environment variable"
conda create --prefix ./env python=3.8 -y
echo [$(date)]:"Activate environment variable"
source activate ./env
echo [$(date)]: "installing dev requirements"
pip install -r requirements_dev.txt
 echo [$(date)]: "Stop"
