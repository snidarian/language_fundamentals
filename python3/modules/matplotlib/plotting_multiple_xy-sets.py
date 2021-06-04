#!/usr/bin/python3
# demonstrating plotting multiple sets of coordinate values


import matplotlib.pyplot as plt


x1 = [17, 14, 32, 45]
x2 = [13, 65, 32, 13]
x3 = [14, 65, 24, 25]

y1 = [31, 13, 56, 24]
y2 = [76, 43, 23, 23]
y3 = [13, 42, 52, 64]


# Plotting multiple sets of coordinate values simply involves calling the .plot() method with more arguments.
plt.plot(x1, y1, 'g--', x2, y2, 'r^', x3, y3, 'bs')


plt.title('Graphs title')
plt.xlabel('label of x axis')
plt.ylabel('label of y axis')


plt.show()
