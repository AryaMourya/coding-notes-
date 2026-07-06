"""Plotting Graphs"""

import numpy as np
import matplotlib.pyplot as plt

## plotting a 2D plot ##

# x = y
x = np.linspace(-10,10,100)
y = x

plt.plot(x,y)
plt.show()

# y = x*2
x = np.linspace(-50,50,100)
y = x**2

plt.plot(x,y)
plt.show()

# y = sin(x)
x = np.linspace(-10,10,100)
y= np.sin(x)

plt.plot(x,y)
plt.show()

# y = xlog(x)
x = np.linspace(-50,50,200)
y = x*np.log(x)

plt.plot(x,y)
plt.show()