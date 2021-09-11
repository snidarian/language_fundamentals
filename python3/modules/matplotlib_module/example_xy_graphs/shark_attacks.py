#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np



years = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


total_attacks = [89, 76, 66, 56, 66, 58, 59, 70, 55, 68, 82, 79, 83]
fatal_attacks = [11, 4, 3, 4, 7, 4, 4, 1, 4, 7, 6, 13, 7]
nonfatal_attacks = [78, 72, 63, 52, 59, 54, 55, 69, 51, 61, 76, 66, 76]


plt.plot(total_attacks, 'b--', label='Total attacks')

plt.plot(fatal_attacks, 'r--', label='Fatal')
plt.plot(nonfatal_attacks, 'g--', label='Non-fatal')


plt.title('Worldwide Shark attacks from 2000 to 2013')
plt.ylabel('Total Number of attacks each year')
plt.xlabel('2000-2013')
plt.xticks(years)



plt.legend()

plt.savefig('sharkattacks.png')

plt.show()



