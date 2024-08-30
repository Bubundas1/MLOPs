import os
from pathlib import Path
import logging

list_of_files=[
".github/workflows/.gitkeep",
"src/__init__.py",
"src/components/__init__.py",
"src/components/data_ingestion.py",
"src/components/data_transformation.py",
"src/components/data_trainer.py",
"src/components/data_evaluation.py",
"src/pipline/__init__.py",
"src/pipline/traning_pipline.py",
"src/pipline/prediction_pipline.py",
"src/utils/__init__.py",
"src/utils/utils.py",
"src/logger/logging.py",
"src/expection/expection.py",
"tests/unit/__init__.py",
"tests/integration/__init__.py",
"init_setup.sh",
"requirements.txt",
"requirements_dev.txt",
"setup.py",
"setup.cfg",
"pyproject.toml",
"tox.inl",
"experiment/experiments.ipynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass # create empty file

print("create succesful!")