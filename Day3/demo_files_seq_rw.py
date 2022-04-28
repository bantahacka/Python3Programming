#! /usr/bin/python 

# Name: demo_files_seq_rw.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Demo how to open close file handles for sequential read+write in txt mode
"""
    Docstring contents here
"""
# Movies dictionary
movies = {
    'marc': ['american psycho', 'american gangster', 'american graffiti'],
    'sean': ['team america', 'sean of the dead', 'next'],
    'tom': ['star wars', 'hans solo', 'rogue one']
}

# Open file handle for writing in text mode
fh_out = open(r"C:\labs\projects\Tyrone_Apr_25_22\Day3\movies.txt", mode="wt")

# Iterate through movies dict and write move info to file handle
for name in movies.keys():
    print(f"{name} - {movies[name]}")
    fh_out.write(f"{name} - {movies[name]}\n")

# Flush buffers and close file handle
fh_out.close()
print("*" * 60)
# Open file handle for reading in text mode
fh_in = open(r"C:\labs\projects\Tyrone_Apr_25_22\Day3\movies.txt", mode="rt")

#text = fh_in.read() # Read entire file to a string object
#text = fh_in.read(30) # Read next 30 chars into a string object
#text = fh_in.readline() # Read next lin in str object
#text = fh_in.readlines()    # Read all lines into a list object
#print(text)
# Iterate through file handle one line at a time
#for line in fh_in.read():   # Read entire file into str obj, iterate through each char in str
    #print(line)

#for line in fh_in.readline():   # Read next line into str obj, iterate through each char in str
    #print(line)

#for line in fh_in.readlines():  # Read lines into list obj, iterate through list
    #print(line, end="")

for line in fh_in:  # Does the same as readlines.
    print(line, end="")

#for line in open(r"C:\labs\projects\Tyrone_Apr_25_22\Day3\movies.txt", mode="rt"):  # Also works!
    #print(line, end="")

# Flush buffers and close file handle
fh_in.close()
