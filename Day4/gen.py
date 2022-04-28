#! /usr/bin/python 

# Name: gen.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Program Description
"""
    Docstring contents here
"""

import decimal

def frange(start, stop=None, step=0.25):
    if stop == None:
        stop = start
        start = 0
    start = decimal.Decimal(str(start))
    stop = decimal.Decimal(str(stop))
    step = decimal.Decimal(str(step))
    num = start
    if step == 0:
        return -1
    while num < stop:
        yield float(num)
        num += step

print(list(frange(1.1, 3)))
print(list(frange(1, 3, 0.33)))
for num in frange(3.142, 12):
    print(f"{num:05.2f}")
print(frange(1,2))

one = list(frange(0, 3.5, 0.25))
two = list(frange(3.5))
if one == two:
    print("Defauts worked!")
else:
    print("Oops! Deafults did not work")
    print("one: ", one)
    print("two: ", two)

