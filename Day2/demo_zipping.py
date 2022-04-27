#! /usr/bin/python 

# Name: demo_zipping.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Combine objects from separate but index related sequences
"""
    Docstring contents here
"""

# Sequences that are separate but have related sequences
students = ['Tyran', 'Tyrone', 'Chris']
heroes = ['Elon Musk', 'Tyrone', 'johnny 6']
fav_bands = ['Spice Girls', 'Metallica', 'Syntatic Sugar']
fav_locations = ['UK', 'Bed', 'Steamhouse']

# Iterate through separate sequences and return index related objects using built in zip() function
for (s, h, fb, fl) in zip(students, heroes, fav_bands, fav_locations):
    print(s + " likes to listen to " + fb + " with " + h + " in " + fl)