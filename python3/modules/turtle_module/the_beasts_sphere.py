#!/usr/bin/python3

import turtle
import math


pen = turtle.Turtle()

pen.color('red', 'yellow')
turtle.bgcolor('black')
pen.speed(0)

while True:
    pen.penup()
    pen.setpos(0, 0)
    pen.pendown()
    for _ in range(400):
        pen.forward(((_%666)))
        pen.left(_%666)
        print(_)
    pen.clear()










