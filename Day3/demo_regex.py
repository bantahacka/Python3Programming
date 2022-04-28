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
#reobj = re.compile(r"^(.)(.).\2\1$") # Pre-compiles regex pattern
# Iterate through file handle and read 1 line at a time
for line in fh_in:
    pass
    #m = reobj.search(line) # Run compiled RE pattern
    #if re.search("^Y.+n$", line):
        #print(line, end="")
    #m = re.search("^the", line) # Match lines starting with the
    #m = re.search("ing$", line) # Match lines ending with ing
    #m = re.search("^[A-Z], line") # Match lines starting with capital
    #m = re.search("^...................$", line) # Match lines exactly 19 chars
    #m = re.search("^.{19}$", line) # Match lines exactly 19 chars
    #m = re.search("[aeiou][aeiou][aeiou]", line) # Match lines with 3 consecutive vowels
    #m = re.search("[aeiou][aeiou][aeiou][aeiou]", line)  # Match lines with 4 consecutive vowels
    #m = re.search("[aeiou]{5,}", line) # Match lines with at least 5 consecutive vowels
    #m = re.search("\.", line) # Match lines with a full stop
    #m = re.search("^[A-Z].*[A-Z]$", line) # Match lines start/ending with capital
    #m = re.search(r"^(.)(.).\2\1$", line) # Match lines with 5 char palindromes (Must be raw string due to back slashes)
    #m = re.search("^([A-Z]).*\1$", line) # Match lines starting/ending with same capital
    #if m:
        #print(line, end="")
    #if line.startswith("Y") and line.rstrip("\n").endswith("n"):    # Pythonic code - string matching
        #print(line, end="")

fh_in.close()   # Flush buffers and close file handles
