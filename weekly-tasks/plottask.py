# plottask.py
# Histogram of a normal distribution of a 1000 values
# Author: John Crumlish

import numpy as np
import matplotlib.pyplot as plt

# Generates Data
data = np.random.normal(5, 2, 1000)

# x & y Values
x = np.arange(0, 11)
y = x**3

# Plotting
plt.hist (data, label="Histogram")
plt.plot(x, y, label="h(x) = x^3")

# Labels
plt.title("Histogram & Function")
plt.xlabel("x Values")
plt.ylabel("y Values")
plt.legend()

# Save Image
plt.savefig("plottask.png")