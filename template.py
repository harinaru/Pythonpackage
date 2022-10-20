import os 
from pathlib import Path
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s]: %(message)s"
)

while True:
    project_name=input("Enter the project name: ")
    if project_name != '':
        break

logging.info(f"Creating Project Name:{ project_name}")

# list of files to create
list_of_files=[
    ".github/workflows/ .gitkeep",


    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",# create to help repoistory conda environment setup
    "requirements.txt",
    "requirements_dev.txt",# dev file for testing
    "setup.py",
    "pyproject.toml", #https://packaging.python.org/en/latest/tutorials/packaging-projects/
    "setup.cfg",
    "tox.ini" # we are creating python package are normally needed to tested on various environment and aslo we need tesrt repoistory

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")

