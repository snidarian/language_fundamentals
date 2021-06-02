#!/usr/bin/python3
# https://www.youtube.com/watch?v=KmziL1djFkQ
# video two in the tutorial series

import turtle
import random
import time

turtle_object = turtle.Turtle()

# list of colors
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

# set colors
turtle_object.color('orange', 'teal')

# set pen width
turtle_object.width(5)

# fill in shape with color
turtle_object.begin_fill()
turtle_object.circle(80)
turtle_object.end_fill()

time.sleep(2)







