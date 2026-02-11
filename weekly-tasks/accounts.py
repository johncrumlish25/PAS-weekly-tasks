# accounts.py
# This program will read an account number and output the last 4 digits
# Author: John Crumlish

# This will appear first
account_number = input("Please enter an 10 digit account number: ")

# Hide first 6 numbers (python uses string[start:end] to access parts of string)
hidden_numbers = "XXXXXX" + account_number[-4:]

print(hidden_numbers)