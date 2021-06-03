#!/usr/bin/python3

import turtle
import random as r
import math as m

pen = turtle.Turtle()
pen.color('red')
pen.getscreen().bgcolor('blue')
pen.speed(0)

def draw_star(size) -> None:
    if size <= 1:
        return
    else:
        for _ in range(5):
            pen.forward(size*5)
            draw_star(size/2)
            pen.left(144)
        



draw_star(50)



turtle.done()