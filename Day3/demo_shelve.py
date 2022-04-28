#! /usr/bin/python 

# Name: demo_shelve.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Demo how to prserve multiple python objects to a shelve file
# like reading/writing to in memory dict, but actually accessing in file dict
"""
    Docstring contents here
"""

import shelve

movies = {
    'marc': ['american psycho', 'american gangster', 'american graffiti'],
    'sean': ['team america', 'sean of the dead', 'next'],
    'tom': ['star wars', 'hans solo', 'rogue one']
}

tv_series = {
    'marc': ['Kardashians', 'only way is essex'],
    'sean': ['great british bake off', 'junior bake off'],
    'tom': ['young sheldon', 'peppa pig']
}

books = {
    'marc': ['the anarchist cook book'],
    'sean': ['K&R standard library'],
    'tom': ['coding in c for bellends']
}

db = shelve.open(r"our_media")
db['films'] = movies
db['tv'] = tv_series
db['books'] = books

print(f"Sean's 2nd favourite TV Series = {db['tv']['sean'][1]}")

db.close()
