#!/usr/bin/python3
# plotting more complex lines with matplotlib


import matplotlib.pyplot as plt
import numpy as np



x = np.arange(0,30, 1)

print(x)

# notice the squared expression below. Matplotlib will plot this. For every x list-value it will use the squared expression to plot it
plt.plot(x*10000, 'g--', linewidth=2, label='Population growth')
plt.plot(x, 'r--', linewidth=3, label='Number of sociopaths')


plt.legend()


# save the graph with the .savefig() method
plt.savefig('mygraph.png')


plt.show()


