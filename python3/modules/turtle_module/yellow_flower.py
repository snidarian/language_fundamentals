#!/usr/bin/python3
# creates yellow flower like shape

import turtle
import random as r


pen = turtle.Turtle()
pen.getscreen().bgcolor('blue')
pen.color('red', 'yellow')
pen.speed(0)


#pen.begin_fill()
for _ in range(70):
    offset = r.randint(0, 1)
    pen.forward(300)
    pen.left(150 + offset)
#pen.end_fill()


# we don't want to do away with the GUI after we're done drawing
turtle.done()



















