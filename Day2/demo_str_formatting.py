#! /usr/bin/python 

# Name: demo_str_formatting.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Demo different ways of formatting strings using concat, escape chars, str methods, .format() and f-strings
"""
    Docstring contents here
"""

planets = { 'Mercury': 57.91,
            'Venus': 108.2,
            'Earth':149.597870,
            'Mars': 227.94
}

# Iterate through key in the dict and display planetary info (Unformatted)
for planet in planets.keys():
    print("\t\t" + planet + ": " + str(planets[planet]) + " Gm " + str(hex(0xff)))

print("-" * 40)

# Iterate through key in the dict and display planetary info (using rjust to right justify)
for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12) + " Gm " + str(hex(0xff)).rjust(6))

print("-" * 40)

# Iterate through key in the dict and display planetary info using .format.
#< is left justify, ^ is center justify, > is right justify, 12(or 6) for padding, .2f for decimal places, # to include hex prefix

for planet in planets.keys():
    print("{0:<12s}: {1:^12.2f} Gm {2:>#6x}  ".format(planet, planets[planet], 0xff))

print("-" * 40)

# Iterate through key in the dict and display planetary info. F Strings introduced from Python 3.5 onwards
for planet in planets.keys():
    print(f"{planet:<12s}: {planets[planet]:^12.2f} Gm {0xff:>#6x} ")

print("-" * 40)

# Iterate through key in the dict and display planetary info. Python 2 way
for planet in planets.keys():
    print(" %12s: %12.2f Gm %#6x  " % (planet, planets[planet], 0xff))
