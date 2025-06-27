from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """This function will return list of requirements"""
    requirement_lst: List[str] = []
    
    try:
        with open("requirements.txt", "r") as f:
            lines = f.readlines()
            ## process each line
            for line in lines:
                requirement= line.strip()
                #ignore empty lines and -e .
                if requirement and not requirement.startswith("-e ."):
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found")
    return requirement_lst


setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Durvankur",
    author_email = "durvankur.rasal48@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements()
)