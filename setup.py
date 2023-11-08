from setuptools import setup, find_packages

setup(
    name='dsss_homework_2',
    version='1.0.0',
    url='https://github.com/SebastianHoefler/dsss_homework_2.git',
    author='Sebastian Hoefer',
    author_email='sebastian.u.hoefler@gmail.com',
    description='Math Quiz',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1'],
)