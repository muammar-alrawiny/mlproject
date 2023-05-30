from setuptools import find_packages,setup
from typing import List

HYFEN_E_DOT ='-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    this function will return the list of requirment
    
    '''
    requirments=[]
    with open(file_path)as file_obj:
        requirments=file_obj.readlines(),
        requirments=[req.replace("\n","")for req in requirments]
        if HYFEN_E_DOT in requirments:
            requirments.remove(HYFEN_E_DOT)
    return requirments        

setup(
    name='mlproject',
    version='0.0.1',
    author='Muammar Alrawiny',
    author_email='muammaralrawiny@gmail.com',
    packages= find_packages(),
    install_requirers = get_requirments('requirments.txt'),
)