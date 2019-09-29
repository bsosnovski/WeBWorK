## To compile WeBWorK_Classlist script into a stand alone program in a Windows machine
## Software: Python 3.7, py2exe, py2win
## In a Command window do the following:
## cd to the directory of the script WeBWorK_Classlist
## python "setup_Win.py" py2exe
##
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(data_files=[],
    options = {'py2exe': {'bundle_files': 3, 'compressed': True}},
    console = [{'script': "WWClasslist.py"}],
    zipfile = "CUNYFirst2WW_converter.zip",
)
