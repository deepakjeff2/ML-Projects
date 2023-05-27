from setuptools import find_packages,setup
from typing import List

hypen = '-e.'
def get_requirements(path:str)->List[str]:
    '''
    This function takes file path of requiremnts.txt and 
    returns the list of requirements
    '''
    requirements=[]
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hypen in requirements:
            requirements.remove(hypen)

    return requirements







setup(
name='mlproject',
version='0.0.1',
author='Deepak',
author_email='deepakjeff2@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)