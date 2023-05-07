from setuptools import find_packages,setup

setup(
    name='mlproject',
    version='0.0.1',
    author='Muammar Alrawiny',
    author_email='muammaralrawiny@gmail.com',
    packages= find_packages(),
    install_requirers = ['pandas','matplotlib','numpy','seaborn']
)