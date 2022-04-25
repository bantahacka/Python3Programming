# Name: ex2.py
# Author: Joe Bloggs, v1.0, contact_email
# Description: Ex 2
"""
    Docstring contents here
"""

fname = "Ty"
lname = "W"

print("Hello %s %s" % (fname, lname))
name_list = [fname, lname]
name_dict = {'first': fname, 'last': lname}
print("List:")
print(name_list)
print("Dict: " + name_dict['first'] + name_dict['last'])
