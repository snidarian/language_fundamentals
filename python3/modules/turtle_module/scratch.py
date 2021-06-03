#!/usr/bin/python3

import turtle
import math


pen = turtle.Turtle()

pen.color('red', 'yellow')

pen.getscreen().bgcolor('teal')
pen.speed(0)

while True:
    for _ in range(10000):
        pen.left(math.sin(_/10)*80)
        pen.forward(math.sqrt(_))











