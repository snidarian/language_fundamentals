#!/usr/bin/python3
# Creating a bar chart


import matplotlib.pyplot as plt
import numpy as np




data = [4, 7, 15, 22, 35, 52, 67]
names= ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# first arguement is a list the names of the bar chart items. The second is a list of their values
plt.bar(names, data, color='green')

# Add grid lines with the .grid() method
plt.grid(color='#f65aba', linestyle='--', linewidth=2, axis='y', alpha=.5)

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Example Bar Graph')


plt.show()

