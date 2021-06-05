#!/usr/bin/python3


import turtle
import math as m

pen = turtle.Turtle()
pen.speed(0)
pen.color('red')
pen.getscreen().bgcolor('black')


def draw_pentagon(size) -> None:
    pen.color('#ffea24')
    if size < 2:
        return
    else:
        for _ in range(5):
            pen.forward(size)
            draw_square(size/2)
            pen.right(72)


def draw_square(size) -> None:
    pen.color('#14ff80')
    if size < 2:
        return
    else:
        for _ in range(4):
            pen.forward(size)
            draw_triangle(size/2)
            pen.right(90)


def draw_triangle(size) -> None:
    pen.color('#ff7124')
    if size < 2:
        return
    else:
        for _ in range(3):
            pen.forward(size)
            draw_pentagon(size/2)
            pen.right(120)



def main(size):
    draw_square(size)



main(200)



turtle.done()

