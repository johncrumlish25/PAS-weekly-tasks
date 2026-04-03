# collatz.py
# Input of integer outputs successive numbers through calculations until it becomes 1
# Author: John Crumlish

number = int(input("Please Enter a Positive Integer: "))

# To make sure the number is positive
while number <=0:
    number = int(input("Please Enter a POSITIVE Number: "))

# Keep printing numbers until it is one
while number !=1:
    print(number, end=" ")

#Even number = divide by 2
    if number % 2 == 0:
        number = number // 2
    
# Odd number = mulitply by 3 and add 1
    else:
        number = number * 3 + 1

print(1)