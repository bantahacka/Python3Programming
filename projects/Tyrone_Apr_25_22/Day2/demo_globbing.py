#! /usr/bin/python 

# Name: demo_globbing.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Display a list of files and directories in home directory
"""
    Docstring contents here
"""

import sys
import os
import glob

if sys.platform == "win32":
    pattern = os.environ['HOMEPATH'] + "\*"
else:
    pattern = os.environ['HOME'] + "/*"

files = glob.glob(pattern)
print("Files matched: ", files)

# Iterate through the files using an iterator for loop
for file in glob.glob(pattern):
    print(file, os.path.getsize(file))
