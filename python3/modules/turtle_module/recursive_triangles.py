#!/usr/bin/python3

import turtle
import random as r
import math as m

pen = turtle.Turtle()
pen.color('blue')
pen.getscreen().bgcolor('orange')
pen.speed(0)



# isolateral triangles
def draw_triangle(size) -> None:
    if size < 1:
        return
    else:
        for _ in range(3):
            pen.forward(size * 1.5)
            draw_triangle(size/2)
            pen.left(120)




draw_triangle(150)




turtle.done()
