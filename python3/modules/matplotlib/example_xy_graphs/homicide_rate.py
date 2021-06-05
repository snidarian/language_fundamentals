#!/usr/bin/python3


import matplotlib.pyplot as plt
import numpy as np

united_states = 3.35
mexico = 19.26
brazil = 29.53
venezuela = 56.33



plt.plot(united_states, '^', label="USA", markersize=10)
plt.plot(venezuela, '^', label="Venezuela", markersize=10)
plt.plot(mexico, '^', label="Mexico", markersize=10)
plt.plot(brazil, '^', label="Brazil", markersize=10)


plt.text(0.03, 28, 'Non-socialist \ncountries with \nfew restrictions \non private gun\n ownership \nshown in blue')

plt.title('By Country Annual Homocide Rate.')
plt.ylabel('Annual homocide rate per 100,000 people')
plt.xticks()


plt.legend()


plt.savefig('homocide_statistics_by_country.png')

plt.show()


























