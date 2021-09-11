#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np



xticks = np.arange(0, 100, 5)
yticks = np.arange(0, 10000, 1000)

x = np.arange(0, 100, 1)


plt.plot(x**2, 'g--', label='How much I dont care')

plt.ylabel('metric units of dont care')
plt.xlabel('Miliseconds')
plt.xticks(xticks)
plt.yticks(yticks)


plt.legend()

plt.savefig('dontcare.png')


plt.show()




