#! /usr/bin/python 

# Name: demo_dict.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: demo how to create, grow and shrink dictionaries. dict  = unordered mutable collection of objs, however ordered in insertion order as of py 3.6
"""
    Docstring contents here
"""

import pprint   #  Pretty Print module

movies = {
    'marc': ['american psycho', 'american gangster', 'american graffiti'],
    'sean': ['team america', 'sean of the dead', 'next'],
    'tom': ['star wars', 'hans solo', 'rogue one']
}

movies['steve'] = ['lolita', 'human centipede', 'hostel']   # Append new key:value pair to existing dictionary

films = movies.copy()   # Copy the dictionary to films
#movies.clear()  # Clear movies dictionary
#movies = {} # Clear movies dictionary
movies.popitem() # Remove last key/object inserted

movies.pop('sean')  # Remove key and its object from dictionary
#print(f"{movies}")
pprint.pprint(movies)
print("-" * 60)
pprint.pprint(films)

print("-" * 60)
# Iterate through dictionary one key at a time
# keys() method returns a VIEW into the dict
for name in movies.keys():
    print(f"{name} likes {films[name]}")

print("-" * 60)
# Iterate through dictionary one value at a time
# keys() method returns a VIEW into the dict
for fav_films in films.values():
    print(f"{fav_films}")

print("-" * 60)
# Iterate through dictionary one value at a time
# keys() method returns a VIEW into the dict
for (name, fav_films) in films.items():
    print(f"{name}'s favourite films = {fav_films}")

print("-" * 60)
print(f"Tom's favourite movie is {films['tom'][0]}")

