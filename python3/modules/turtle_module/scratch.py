#!/usr/bin/python3

import turtle
import math


pen = turtle.Turtle()

pen.color('red', 'yellow')
turtle.bgcolor('teal')
pen.speed(0)

while True:
    for _ in range(10000):
        pen.forward((math.sqrt(_) * 10))
        pen.left(math.sqrt(_))
        pen.right(50)
        pen.forward((math.sqrt(_) * math.sqrt(_)))
        pen.left(310)











