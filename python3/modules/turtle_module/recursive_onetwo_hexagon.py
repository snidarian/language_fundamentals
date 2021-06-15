#!/usr/bin/python3


import turtle as t
import math as m
import random as r

pen = t.Turtle()
pen.color('red')

color_set = ['red', 'yellow', 'blue', 'orange', 'green', 'purple', 'cyan', 'white', 'maroon', 'pink']
pen.getscreen().bgcolor('black')
pen.speed(0)


pen.left(45)

def hexagon_one(size) -> None:
    if size < 1:
        return
    else:
        pen.color(r.choice(color_set))
        for _ in range(6):
            pen.forward(size)
            hexagon_two(size/4)
            pen.right(60)


def hexagon_two(size) -> None:
    if size < 1:
        return
    else:
        pen.color(r.choice(color_set))
        for _ in range(6):
            pen.forward(size)
            hexagon_one(size/2)
            pen.left(60)





hexagon_one(150)






t.done()

