#! /usr/bin/python 

# Name: demo_lotto.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: This program will generate 6 random numbers
"""
    Docstring contents here
"""

from random import randint

lotto = []  # Empty list

while len(lotto) < 6:
    num = randint(1, 50)
    if num not in lotto:
        lotto.append(num)
    else:
        continue

lotto.sort()
print(lotto)
