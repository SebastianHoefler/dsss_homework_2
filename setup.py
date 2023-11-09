from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='1.0.0',
    url='https://github.com/SebastianHoefler/dsss_homework_2.git',
    author='A scored mathquiz for elementary math problems',
    author_email='sebastian.u.hoefler@gmail.com',
    description='Math Quiz',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1'],
)