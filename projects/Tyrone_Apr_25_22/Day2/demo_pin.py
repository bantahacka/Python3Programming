#! /usr/bin/python 

# Name: demo_pin.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Program to simulate a high street bank
"""
    Docstring contents here
"""
import getpass

master_pin = "0123"
pin = None  # None Type
attempts = 3
# Repeat until a correct pin is entered

while pin != master_pin and attempts > 0:
    pin = getpass.getpass("Enter a PIN (%d tries remaining): " % attempts)
    if pin == master_pin:
        print("Valid PIN!")
        break
    else:
        print("Invalid PIN!")
        attempts -= 1

else:
    # Executes when while loop becomes false i.e. when > 3 attempts
    print("Too many attempts.")
    print("Your card has been retained. Have a nice day!")

print("Done")
