#!/usr/bin/python3


import turtle
import math as m

pen = turtle.Turtle()
pen.speed(0)
pen.color('red')
pen.getscreen().bgcolor('blue')


def draw_pentagon(size) -> None:
    pen.color('red')
    if size < 2:
        return
    else:
        for _ in range(5):
            pen.forward(size*2)
            draw_triangle(size/2)
            pen.right(72)


def draw_triangle(size) -> None:
    pen.color('orange')
    if size < 2:
        return
    else:
        for _ in range(3):
            pen.forward(size*2)
            draw_pentagon(size/2)
            pen.right(120)




draw_triangle(100)



turtle.done()



