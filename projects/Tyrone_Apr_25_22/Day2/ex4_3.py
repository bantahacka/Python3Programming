#! /usr/bin/python 

# Name: ex4_3.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Ex 4 q 3
"""
    Docstring contents here
"""

for line in open('messier.txt', encoding='latin_1'):
    if not line:
        break
    if line.startswith('M'):
        mes_num = line[:6].rstrip()
        com_name = line[6:40].rstrip()
        if not com_name:
            com_name = 'no name'
        obj_type = line[40:64].rstrip()
        const = line[64:].rstrip()
        print(f"|{mes_num}|{com_name}|{obj_type}|{const}")
