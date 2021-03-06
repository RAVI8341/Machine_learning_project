#from gettext import install
from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing_predictor"
VERSION="0.0.1"
AUTHOR="ravi"
DESCRIPTION="tHIS IS FORST FSDS ML PROJECT"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirments_list()->List[str]:
    """
    Description: This function is going to return list or requirment mention in requirments.txt file

    return this function is going to return a list which contain name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")
setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirments_list()
)

#if __name__=="__main__":
    #print(get_requirments_list())