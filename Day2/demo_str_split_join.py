#! /usr/bin/python 

# Name: demo_str_split_join.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Demo how to split and rejoin strings using the .split and .join methods
"""
    Docstring contents here
"""

# ROOT USER login details from /etc/passwd
# Want to make some changes, but str objects are immutable
line = "root:x:0:0:The Super User:/root:/bin/ksh"
print("Original: ", line)
fields = line.split(":") # Returns a list of objects that are mutable
print(fields)
fields[4] = "The Administrator"
fields[-1] = "/bin/bash"
print(fields)
# Rejoin fields with colon and overwrite line variable
line = ":".join(fields)
print("New: ", line)
