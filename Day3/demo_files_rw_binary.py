#! /usr/bin/python 

# Name: demo_files_rw_binary.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Program Description
"""
    Docstring contents here
"""
# Movies dictionary
movies = {
    'marc': ['american psycho', 'american gangster', 'american graffiti'],
    'sean': ['team america', 'sean of the dead', 'next'],
    'tom': ['star wars', 'hans solo', 'rogue one']
}

# Open file handle for writing in binary mode
fh_out = open(r"C:\labs\projects\Tyrone_Apr_25_22\Day3\movies2.txt", mode="wb")

# Iterate through movies dict and write move info to file handle
for name in movies.keys():
    print(f"{name} - {movies[name]}".encode())
    fh_out.write(f"{name} - {movies[name]}\n".encode())

# Flush buffers and close file handle
fh_out.close()
print("*" * 60)
# Open file handle for reading in binary mode

fh_in = open(r"C:\labs\projects\Tyrone_Apr_25_22\Day3\movies2.txt", mode="rb")


for line in fh_in:
    print(line.decode(), end="")
    print(line)
