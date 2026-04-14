# plottask.py
# Histogram of a normal distribution of a 1000 values
# Author: John Crumlish

# References:
# https://www.w3schools.com/python/matplotlib_histograms.asp
# https://numpy.org/doc/stable/reference/generated/numpy.arange.html

import numpy as np
import matplotlib.pyplot as plt

# Generate Data
data = np.random.normal(5, 2, 1000)

# x & y Values
x = np.arange(0, 11)
y = x**3

# NORMALISE the function so it fits the histogram scale
y = y / max(y)

# Plotting
plt.hist(data, bins=30, density=True, alpha=0.6, label="Histogram")
plt.plot(x, y, label="Scaled h(x) = x^3")

# Labels & Styling
plt.title("Histogram of Normal Distribution and Scaled h(x) = x^3")
plt.xlabel("x Values")
plt.ylabel("Density / Scaled Value")
plt.legend()
plt.grid()

# Save Image
plt.savefig("plottask.png")