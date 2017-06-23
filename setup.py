'''
This file should exists at the root of your project directory.

“setup.py” serves two primary functions:

It’s the file where various aspects of your project are configured. The primary feature of setup.py is that it contains a global setup() function. The keyword arguments to this function are how specific details of your project are defined. The most relevant arguments are explained in the section below.
It’s the command line interface for running various commands that relate
to packaging tasks. To get a listing of available commands, run python
setup.py --help-commands.

The primary feature of setup.py is that it contains a global setup() function. The keyword arguments to this function are how specific details of your project are defined.
'''
from distutils.core import setup
import py2exe

setup(
    name="Mailer",
    version="1.0",
    author="Sandeep Bandi",
    author_email="bsandyy@gmail.com",
    description=("The purpose of this script is to say HI to the name given in conf file"),
    license="MIT",
    console=['hi.py'])

# data_files=[('config', ['conf.ini'])],
