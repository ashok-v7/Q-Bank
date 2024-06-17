import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
logging.info("welcome to team prj")

# folders and files as below
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirement.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filepath = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # print(filedir)
    # print(filepath)
