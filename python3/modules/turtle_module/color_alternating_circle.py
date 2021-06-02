#!/usr/bin/python3
# This color draws itself repeatedly in different color patterns
# randomizes colors of screen, circle-line and circle-fill for each draw

import turtle
import random
import time

color_list = ['red', 'green', 'purple', 'blue', 'yellow', 'orange', 'teal', 'maroon', 'black', 'pink', 'violet', 'cyan']

# create turtle object
turtle_object = turtle.Turtle()


while True:
    turtle.bgcolor(color_list[random.randint(0, (len(color_list) -1))])
    color1 = color_list[random.randint(0, (len(color_list) -1))]
    color2 = color_list[random.randint(0, (len(color_list) -1))]
    random_width = random.randint(0, 111)
    # set circle fill and circle outline with random colors from 'color_list'
    turtle_object.color(color1, color2)
    # set random pen width
    turtle_object.width(random_width)
    # fill in shape with color
    turtle_object.begin_fill()
    turtle_object.circle(random.randint(45, 160))
    turtle_object.end_fill()
    time.sleep(.5)
    # clears image after every drawing
    turtle_object.clear()
    turtle_object.speed(random.randint(0, 10))
    turtle_object.shape('arrow')





