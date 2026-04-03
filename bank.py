# bank.py
# program will print out sum of two amounts (cents) into final sum (Euros)
# Author: John Crumlish

# Prompts user to add their amounts
amount1 = int (input("Enter First Amount:"))
amount2 = int (input("Enter Second Amount:"))
answer = amount1 + amount2

# Make answer in readable money format
TotalCents = answer
euros = answer / 100

# Final Sum (This is the only part I had to look up as I did not know how to add Euro symbol)
print(f"The Sum of These is: €{euros:.2f}")