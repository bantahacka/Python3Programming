#! /usr/bin/python 

# Name: demo_counter_loops.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Repeat a block of commands a specific number of repetitions using a counter while or for loop
"""
    Docstring contents here
"""

count = 0   # Counter initialization
while count < 10:
    print(count)
    count += 1

# range (start, stop, step)
for i in range(0, 10, 2):
    print(i)

# range (start, stop, step=1)
for i in range(0, 10):
    print(i)

# range (start=0, stop, step=0)
for i in range(10):
    print(i)


var = input("Enter a positive integer: ")

if not var.isdecimal:
    print("Positive integer not entered!")
    exit(1)
else:
    for var in range(int(var), -1, -2):
        print(var)
