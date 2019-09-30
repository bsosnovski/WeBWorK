## Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application
#
# To create a stand alone app:
# Go to terminal
# Type: cd /Users/Beebee/Desktop/wwclasslist
# Then type: python setup_Win2.py build

application_title = "CUNYFirst2WW_Converter" #what you want to application to be called
main_python_file = "WWClasslist.py" #the name of the python file you use to run the program

import sys
import cx_Freeze
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["atexit","re", "os"]


setup(
        name = application_title,
        version = "2.0",
        description = "Script to convert CUNY Portal Rosters to a WeBWorK classlist file ",
        author="Bianca Sosnovski, QCC",
        options = {"build_exe" : {"includes" : includes }},
        executables = [Executable(main_python_file, base = base)])


