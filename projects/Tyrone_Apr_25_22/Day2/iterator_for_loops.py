#! /usr/bin/python 

# Name: iterator_for_loops.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Demo on how to iterate through collections/sequences (strings, tuples, lists, dicts, sets, file handles etc) using an iterator for loop
"""
    Docstring contents here
"""

students = ['adam', 'bill', 'charlie', 'dave', 'edgar']

# Iterate through the list, using an ITERATOR for loop
for name in students:
    print(name)

# Iterate through list and modify the objects
for name in students:
    print(name.upper())

print("Students =", students)


# Iterate through list and modify the objects using enumerate function
for idx, name in enumerate(students):
    students[idx] = name.upper()

print("Students upper =", students)
