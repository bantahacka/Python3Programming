#! /usr/bin/python
# Exercise 6, string formatting and regular expressions.
import re

infile = open('postcodes.txt', 'r')

# Variables for counting valid and invalid codes (part b)
valid = 0
invalid = 0
valpat = re.compile("[A-Z]{1,2}\d{1,2}[A-Z]? \d[A-Z]{2}")

for postcode in infile:
    # The variable 'postcode' contain the line read from the file.
    
    # Ignore empty lines.
    if postcode.isspace(): continue
    
    # TODO (a): Remove newlines, tabs and spaces.
    postcode = re.sub(r"[\s\n]", r"", postcode)
    
    # TODO (a): Convert to uppercase.
    postcode = postcode.upper()

    # TODO (a): Insert a space before the final digit and 2 letters.
    postcode = re.sub(r"(\d[A-Z]{2})$", r" \1", postcode)
    
    # Print the reformatted postcode.
    print(postcode)

    # TODO (b) Validate the postcode, returning a match object 'm'.
    m = valpat.match(postcode)
    #m = re.match(valpat, postcode)   # TODO (b) Replace this line with a call to re.match().
    
    if m:
        valid = valid + 1
    else:
        invalid = invalid + 1
        

infile.close()

# TODO (b) Print the valid and invalid totals.
print(f"Valid postcodes: {valid}")
print(f"Invalid postcodes: {invalid}")
