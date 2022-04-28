#! /usr/bin/python 

# Name: .py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Demo how to yeild one object at a time using generator func (lazy list)
"""
    Docstring contents here
"""

def get_numbers():
    """Return entire list of numbers    """
    print("Executing get_numbers()..")
    numbers = []
    for num in range(0, 100):
        numbers.append(num)
    return numbers

#for z in get_numbers():
    #print(z)

def generate_numbers():
    """Yeild one obj from collection at a time"""
    print("Executing generate_numbers()")
    for num in range(0,100):
        yield num

#for z in generate_numbers():
    #print(z)



# Alternatively use a while loop to request next yield object
gen = generate_numbers()
while True:
    num = next(gen, -1)
    if num != -1:
        print(num)
    else:
        break

# Manually request yielded object
gen1 = generate_numbers()
num1 = next(gen1, -1)
num2 = next(gen1, -1)
num3 = next(gen1, -1)
print(num1, num2, num3)