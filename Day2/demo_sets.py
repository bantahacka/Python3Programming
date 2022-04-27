#! /usr/bin/python 

# Name: demo_sets.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Demo how to create, grow and shrink and combine sets (unordered mutable collection of objects) = unique objects = removes duplicates
"""
    Docstring contents here
"""

marvel_fans = {'sean', 'marc', 'adam', 'tyrone', 'steve', 'donald'}
dc_fans = set()     # empty set

dc_fans.add('mike')
dc_fans.add('steve')
dc_fans.add('donald')

print(f"Marvel fans = {marvel_fans}")
print(f"DC Fans = {dc_fans}")
comic_fans = dc_fans.copy()
# comic_fans.clear()
# comic_fans = set()
# dc_fans.pop()   # Remove the next object returned
dc_fans.remove('steve')
print(f"DC Fans = {dc_fans}")

# Combine sets using set methods
print(f"Fans of Marvel or DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of Marvel and DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of Only Marvel or DC but not both = {marvel_fans.symmetric_difference(dc_fans)}")
# Combine sets using set operators
print(f"Fans of Marvel or DC = {marvel_fans | dc_fans}")
print(f"Fans of Marvel and DC = {marvel_fans & dc_fans}")
print(f"Fans of ONLY Marvel = {marvel_fans - dc_fans}")








































print(f"Fans of Only Marvel or DC but not both = {marvel_fans ^ dc_fans}")
