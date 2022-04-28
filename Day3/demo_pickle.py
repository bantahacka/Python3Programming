#! /usr/bin/python 

# Name: demo_pickle.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: demo how to preserve one python object to a file, inc data plus structure
"""
    Docstring contents here
"""

import pickle
import pprint
import gzip

movies = {
    'marc': ['american psycho', 'american gangster', 'american graffiti'],
    'sean': ['team america', 'sean of the dead', 'next'],
    'tom': ['star wars', 'hans solo', 'rogue one']
}

#with open(r"movies.p", mode="wb") as fh_out:
with gzip.open(r"movies.pgz", mode="wb") as fh_out:
    pickle.dump(movies, fh_out)
    # protocol=0: write as ascii
    # protocol=1: write as binary (py2+3)
    # protocol=2 write as BINARY (py3) - More efficient
    # protocol=3 or pickle.DEFAULT_PROTOCOL write as BINARY (py3) - Even more efficient
    # protocol=4 or pickle.HIGHEST_PROTOCOL write as BINARY (py3) - Most efficient

with gzip.open(r"movies.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)

pprint.pprint(movies)
print("-" * 70)
pprint.pprint(films)