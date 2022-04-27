#! /usr/bin/python 

# Name: lists_demo.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: demo how to create, grow and shrink lists and also how to index, slice and use lists

"""
    Docstring contents here
"""
# List is a mutable ordered collection/sequence of objects
movies = ['scarface', 'sharknado', 'snakes on a plane', 'gremlins']
tv_series = ['the boys', 'reacher', 'bobba fett']
print(type(movies))
print(isinstance(movies, list))
print(f"Movies = {movies}")
print(f"1st object  = {movies[0]}")
print(f"last object = {movies[-1]}")
print(f"last 3 objects = {movies[-3:]}")

print(f"Length of movies list = {len(movies)}")

movies.append("White Chicks")
print(f"Movies = {movies}")
print(f"Length of movies list = {len(movies)}")

movies.extend(["stand by me", "the meg"]) # Extend the list by multiple objects
print(f"Movies = {movies}")
print(f"Length of movies list = {len(movies)}")
movies.insert(0, "texas chainsaw massacre")
movies.insert(3, "bruno")
print(f"{movies}")
last = movies.pop()    # Removes and returns last object
first = movies.pop(0)   # Removes and returns object at given index
print(f"First: {first}  Last: {last}  Movies: {movies}")
#combo = movies.copy()
#combo.extend(tv_series)
#print(f"{combo}")
#films = movies.copy() # Copy movies to films
#films.clear() # Empty the list
#print(f"Favourite movies and tv shows: { movies + tv_series}")