#! /usr/bin/python 

# Name: demo_regex.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Demo how to match string data using regular expressions/regex and the re module
"""
    Docstring contents here
"""

import re
# Open file handle for reading in text mode
fh_in = open(r"words", "rt")

# Iterate through file handle and read 1 line at a time
for line in fh_in:
    if re.search("^Y", line):
        print(line, end="")
    #if line.startswith("Y") and line.rstrip("\n").endswith("n"):    # Pythonic code - string matching
        #print(line, end="")

fh_in.close()   # Flush buffers and close file handles
