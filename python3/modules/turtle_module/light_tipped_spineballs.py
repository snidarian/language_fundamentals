#!/usr/bin/python3


import turtle as t
import math as m



pen = t.Turtle()
pen.color('yellow')
pen.speed(0)
pen.getscreen().bgcolor('blue')


color_list = ['red', 'yellow', 'green', 'pink']


def draw_straight_line(size) -> None:
    if size < 20:
        pen.color('red')
        return
    else:
        for _ in range(10):
            pen.color('red')
            pen.forward(size)
            pen.color('green')
            pen.forward(size/10)
            pen.color('#14ff80')
            pen.forward(size/10)
            pen.backward(size/10)
            pen.color('green')
            pen.backward(size/10)
            pen.color('red')
            draw_straight_line(size/2)
            pen.backward(size)
            pen.right(36)





draw_straight_line(100)




t.done()

