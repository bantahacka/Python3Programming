#! /usr/bin/python 

# Name: banking.py
# Author: Joe Bloggs
# Revision: v1.0
# Description: program is mBA (mini Baning App)
"""
    mBA (mini Banking App) with deposit and withdrawal facilities
"""

import sys

def deposit(bank_balance):
    """ Deposit monies and return updated bank balance """
    amount = float(input("Enter monies to deposit: "))
    if amount < 0:
        print("Invalid amount")
        return bank_balance
    bank_balance += amount
    print(f"Deposited \N{euro sign}{amount:.2f}")
    return bank_balance


def withdraw(bank_balance):
    """ Withdraw monies and return updated bank balance """
    amount = float(input("Enter monies to withdraw: "))
    if amount < 0:
        print("Invalid amount")
        return bank_balance
    bank_balance -= amount
    if bank_balance < 0:
        bank_balance += amount
        print("Insufficient funds.")
        return bank_balance
    print(f"\N{euro sign}{amount:.2f} withdrawn")
    return bank_balance


def main():
    bank_balance = 0
    print(f"Welcome to mBA - mini Banking App!")

    while True:
        menu = f"""
                mBA Menu
                --------
                Current balance \N{euro sign}{bank_balance:.2f}
                1. Deposit monies
                2. Withdraw monies
        """
        print(menu)
        choice = input("Enter option (1-2, q=quit): ")
        if choice == "1":
            bank_balance = deposit(bank_balance)
        elif choice == "2":
            bank_balance = withdraw(bank_balance)
        elif choice.lower() == "q":
            break
        else:
            print("Invalid option")
            continue

    print("Done")
    sys.exit(0)

if __name__ == "__main__":
    main()
