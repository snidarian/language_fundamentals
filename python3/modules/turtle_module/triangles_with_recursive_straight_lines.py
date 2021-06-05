#!/usr/bin/python3


import turtle as t
import math as m



pen = t.Turtle()
pen.color('yellow')
pen.speed(0)
pen.getscreen().bgcolor('blue')


color_list = ['red', 'yellow', 'green', 'pink']


def draw_straight_line(size) -> None:
    if size < 1:
        return
    else:
        for _ in range(3):
            pen.forward(size*2)
            draw_straight_line(size/2)
            pen.backward(size*2)
            pen.right(120)





draw_straight_line(100)




t.done()

