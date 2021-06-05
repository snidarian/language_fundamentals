#!/usr/bin/python3


import matplotlib.pyplot as plt
import numpy as np



# variables lists that contain the values for the coordinates to be plotted
x = [1, 2, 10, 15, 30, 20]
y = [2, 4, 20, 30, 60, 40]
z = [2 ,3, 5, 59, 110 ,100]

# plots the xy coordinates
# optional third argument to the plot() method is color and coordinate formatting. The default is 'b-' for a blue line. 
# 'ro' renders red orbs and 'g^' renders green caret-marks. green squares: 'gs', red dashes: 'r--'
plt.plot(x, 'r-', label='label0', linewidth=3, linestyle='--')
plt.plot(y, 'gs', label='label1', linewidth=2, markersize=7, markeredgecolor='red')
plt.plot(z, 'y--', label='label2', marker='^', markersize='15', markeredgecolor='b')


# Gives a title to the graph
plt.title('basic graph demonstrating matplotlib')

# Giving a names label to the x and y axises on the graph
plt.xlabel('x values')
plt.ylabel('y values')


# You can manually specify the x and y ticks on the graph
#plt.xticks([1, 4, 5, 50])
#plt.yticks([2, 5, 7, 50])


# Shows legend label for each coordinate set (specified with label='example0')
plt.legend()


# shows the graph
plt.show()




