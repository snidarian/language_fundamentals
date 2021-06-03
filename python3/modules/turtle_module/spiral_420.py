#!/usr/bin/python3

import turtle
import math



pen = turtle.Turtle()
pen.color('yellow', 'red')
pen.speed(0)
turtle.bgcolor('green')


for _ in range(100000):
    pen.forward(math.sqrt(420))
    pen.left(_%420)


turtle.done()








