#!/usr/bin/python3
# Bar chart using mutliple dimensions


import matplotlib.pyplot as plt
import numpy as np


data1 = [3, 7, 5, 9, 2]
data2 = [8, 5, 6, 3, 4]
data3 = [3, 3, 7, 6, 9]

names = [1, 2, 3, 4, 5]

# variable used to store width value used to place graph values side by side
width=.3

plt.bar(np.arange(len(data1)), data1, width=width)
plt.bar(np.arange(len(data2)) + width, data2, width=width)


plt.title('Example multi-dimensional graph')
plt.xlabel('X axis')
plt.ylabel('Y axis')




plt.show()








