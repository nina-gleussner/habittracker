from setuptools import setup, find_packages
from pathlib import Path
from done import database
from done import exampledata

def read_requirements():
    with open("requirements.txt") as req:
        content = req.read()
        requirements = content.split("\n")

    return requirements


setup(
    name="done",
    version="0.1",
    packages=find_packages(),
    install_requires=read_requirements(),
    entry_points='''
    [console_scripts]
    done=done.cli:cli
    '''
)

# setup empty __pycache__ folders
directory_path = Path("__pycache__")
done_path = Path("done/__pycache__")

done_path.mkdir(exist_ok = True)
directory_path.mkdir(exist_ok = True)

# creates aatabase
database.CreateDatabase()
# load in sample data
exampledata.LoadData()
