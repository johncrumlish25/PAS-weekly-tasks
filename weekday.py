# weekday.py
# Outputs whether or not today is a weekday
# Author: John Crumlish

# Reference:
# https://www.w3schools.com/python/python_datetime.asp

import datetime

# Get today's day
today = datetime.datetime.today().weekday()

# Weekdays: Monday=0,....,Sunday=6
if today < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")