#! /usr/bin/python 

# Name: demo_unicode_charset.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Program will display entire unicode charset in a table with 16 chars per row
"""
    Docstring contents here
"""

import sys

# Iterate through all the char positions from 0 to 65536
# Using an iterator for loop plus the range function

for pos in range(0,65536, 1):
    try:
        print(chr(pos), end=" ")
        if pos % 16 == 0:
            print("")
    except UnicodeEncodeError:
        print("\N{pile of poo}", file=sys.stderr)
