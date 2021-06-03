#!/usr/bin/python3

import turtle
import math


pen = turtle.Turtle()

pen.color('green', 'yellow')
pen.getscreen().bgcolor('red')
pen.speed(0)

while True:
    for _ in range(10000):
        pen.forward((math.sqrt(_) * 10))
        pen.left(math.sqrt(_))
        pen.right(50)
        pen.forward((math.sqrt(_) * math.sqrt(_)))
        pen.left(210)











