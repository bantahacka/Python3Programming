#! /usr/bin/python  # Ignored on Windows, for Linux only.

# Python Comments
# Name: first.py
# Author: Joe Bloggs, v1.0, contact_email
# Description: This is our first program
"""
    Docstring contents here
"""

# name = "Bob Jones"
name = input("Enter your name: ")

print("My name is", name)   # Interprets to print("My name is", name, sep = " ")
print("My name is " + name)
print("My name is %s" % name)

import math
print("Cosine of 0.5=", math.cos(0.5))
