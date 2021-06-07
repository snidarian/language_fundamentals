#!/usr/bin/python3


import turtle as t
import math as m
import random as r

pen = t.Turtle()
pen.color('red')

color_set = ['red', 'yellow', 'blue', 'orange', 'green', 'purple', 'cyan', 'white', 'maroon', 'pink', 'black']
pen.getscreen().bgcolor(r.choice(color_set))
pen.speed(0)




def draw_random(size) -> None:
    if size < 2:
        return
    else:
        pen.color(r.choice(color_set))
        shape = r.randint(2, 8)
        for _ in range(shape):
            pen.forward(size)
            draw_random(size/2)
            pen.right((360/shape))


def hexagon_one(size) -> None:
    if size < 1:
        return
    else:
        pen.color('yellow')
        for _ in range(6):
            pen.forward(size)
            hexagon_two(size/4)
            pen.right(60)


def hexagon_two(size) -> None:
    if size < 1:
        return
    else:
        pen.color('green')
        for _ in range(6):
            pen.forward(size)
            hexagon_one(size /2)
            pen.right(60)





draw_random(100)






t.done()

