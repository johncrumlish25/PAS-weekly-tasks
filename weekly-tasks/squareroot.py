# squareroot.py
# Takes a positive floating-point number as input and outputs an approximation of its square root
# Author: John Crumlish

def sqrt(n):
    guess = n / 2
    while abs(guess * guess - n) > 0.000001:
        guess = 0.5 * (guess + n / guess)
    return guess


number = float(input("Enter a positive number: "))

if number < 0:
    print("Number must be positive.")
else:
    print("Approximate square root:", sqrt(number))