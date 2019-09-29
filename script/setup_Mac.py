# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt5app.py is a very simple type of PyQt5 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application
#
# To create a stand alone app:
# Go to terminal
# Type: cd /Users/Beebee/Desktop/Classroster_program
# Then type: python3.7 setup_Mac.py bdist_mac

application_title = "CUNYFirst2WW_Converter" #what you want to application to be called
main_python_file = "WWClasslist.py" #the name of the python file you use to run the program

import sys
import cx_Freeze
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"
    else None

includes = ["atexit","re"]
#excludes = ["tkinter"]

setup(
        name = application_title,
        version = "2.0",
        description = "Script to convert CUNY Portal Rosters to a WeBWorK classlist file ",
        author="Bianca Sosnovski, QCC",
        options = {"build_exe" : {"includes" : includes }},
        executables = [Executable(main_python_file, base = base)])

