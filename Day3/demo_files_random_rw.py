#! /usr/bin/python 

# Name: demo_files_random_rw.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Demo how to open/close file handles for random read/write using .seek and .tell methods
"""
    Docstring contents here
"""


with open(r"movies.txt", mode="rt") as fh_in:
    fh_in.seek(60, 0)   # Seek to char position from start of file
    text = fh_in.read(30)  # Read next 30 chars
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

with open(r"movies2.txt", mode="rb") as fh_in:
    fh_in.seek(-120, 2)   # Seek to char position from start of file
    text = fh_in.read(30)  # Read next 30 chars
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(-60, 1)  # Seek to char position from start of file
    text = fh_in.read(30)  # Read next 30 chars
    print(f"Text at {fh_in.tell() - len(text)} = {text}")