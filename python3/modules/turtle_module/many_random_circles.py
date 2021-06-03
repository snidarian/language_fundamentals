#!/usr/bin/python3
# draws many random circles of random, widths, outlines, fills, backgrounds amounts and speeds.

import turtle
import time
import random


# first create turtle object
turtle_object = turtle.Turtle()

# List that will contain the string values for our colors
#color_list = ['black', 'teal', 'orange', 'green']
#color_list = 


# set max width of each individual circle
circle_maxwidth = 45


# one color combinations list is chosen randomly and assigned to color_list variable
color_list = random.choice([
    ['green', 'orange', 'red'],
    ['black', 'white', 'yellow'],
    ['purple', 'pink', 'violet', 'yellow'],
    ['teal', 'black', 'cyan', 'orange', 'red'],
    ['black', 'white'],
    ['red', 'green', 'blue'],
    ['black', 'teal', 'orange', 'green'],
    ['red', 'yellow', 'blue', 'green', 'teal', 'pink', 'maroon', 'violet', 'purple', 'black', 'orange', 'cyan']
])


# function that repositions turtle object on graph and draws random circle
def draw_random_circle() -> None:
    x_value = random.randint(-700, 700)
    y_value = random.randint(-500, 500)
    turtle_object.setpos(x_value, y_value)
    turtle_object.pendown()
    color1 = color_list[random.randint(0, (len(color_list) -1))]
    color2 = color_list[random.randint(0, (len(color_list) -1))]
    turtle_object.color(color1, color2)
    turtle_object.begin_fill()
    turtle_object.circle(random.randint(0, circle_maxwidth))
    turtle_object.end_fill()
    




# while loop that continually calls draw circle function and recolors screen
while True:
    turtle_object.getscreen().bgcolor(color_list[random.randint(0, (len(color_list) - 1))])
    turtle_object.shape('turtle')
    turtle_object.speed(0)
    # each time background color changes draw variable amount of circles with a for loop in range(random integer) that calls the draw_random_circle() function
    for _ in range(random.randint(0, 10)):
        turtle_object.penup()
        draw_random_circle()


