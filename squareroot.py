# squareroot.py
# Takes a positive floating-point number as input and outputs an approximation of its square root
# Author: John Crumlish

precision = 0.000001  # Controls how accurate the result is

# Function to calculate square root using the Newton-Raphson method
def sqrt(n):
    guess = n / 2  # Initial guess

    # Repeat until the guess is accurate enough
    while abs(guess * guess - n) > precision:
        # Newton-Raphson formula to improve the guess
        guess = 0.5 * (guess + n / guess)

    return guess


# Ask user for input
number = float(input("Enter a positive number: "))

# Check if number is valid
if number < 0:
    print("Number must be positive.")
else:
    # Print the approximate square root
    print("Approximate square root:", sqrt(number))