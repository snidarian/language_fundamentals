#!/usr/bin/python3
# plotting more complex lines with matplotlib


import matplotlib.pyplot as plt
import numpy as np



x = np.arange(0,10000, 1)

print(x)

# notice the expression below. Matplotlib will plot this. For every x list-value it will use calculate the expression to plot it
plt.plot(x, 'g--', linewidth=2, label='Population')
plt.plot(x*.03, 'r--', linewidth=3, label='Number of sociopaths')

plt.title('3 Male (1 female) sociopaths in every 100 persons')

plt.legend()


# save the graph with the .savefig() method
plt.savefig('mygraph.png')


plt.show()


