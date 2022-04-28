#! /usr/bin/python 

# Name: account.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: program is mBA - minions Banking App - used by millions of Minions!
"""
    Withdraw, deposit and display banking info
"""

import sys
import banking


def display_info(bal, scode):
    """ Display banking info """
    print(f"Current balance: \N{euro sign}{bal:.2f}  Sort code:{scode}")
    return None


def main():
    bank_balance = 56789.43
    sort_code = "80-45-37"

    name = input("Enter your name: ")
    print(f"Welcome {name} to the Minions Banking App!")

    while True:
        menu = f"""
                Menu Options
                ------------
                1. Display account info
                2. Deposit monies
                3. Withdraw monies
        """
        print(menu)
        answer = input("Enter choice (1-3, q=quit): ")
        if answer == "1":
            display_info(bank_balance, sort_code)
        elif answer == "2":
            bank_balance = banking.deposit(bank_balance)
        elif answer == "3":
            bank_balance = banking.withdraw(bank_balance)
        elif answer.lower() == "q":
            break
        else:
            print("Invalid option!")
            continue

    print(f"Thank you {name} for using our App!")

    sys.exit(0)

if __name__ == "__main__":
    main()
