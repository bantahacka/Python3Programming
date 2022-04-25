# Name: pickacard.py
# Author: Joe Bloggs, v1.0, contact_email
# Description: Allows user to pick a card
"""
    Docstring contents here
"""

import showcard

while 1:
    user_input = input("Pick a card (1-52): ")
    if not user_input.isdigit():
        print("Invalid card value")
        continue
    if not 0 < int(user_input) < 53:
        print("Invalid card value")
        continue

    user_timeout = input("How long do you want to display the card for in seconds (Max 60 seconds): ")
    if not user_timeout.isdigit():
        print("Invalid timeout value")
        continue
    user_timeout = int(user_timeout)
    if not 0 < user_timeout < 61:
        print("Invalid timeout value")
        continue

    filename = "BMP"+user_input+".GIF"
    showcard.set_timeout(user_timeout)
    showcard.display_file(filename)
