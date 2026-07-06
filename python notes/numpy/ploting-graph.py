"""Plotting Graphs"""

import numpy as np
import matplotlib.pyplot as plt

## plotting a 2D plot ##

# x = y
x = np.linspace(-10,10,100)
y = x

plt.plot(x,y)
plt.show()