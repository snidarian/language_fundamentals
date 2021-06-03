#!/usr/bin/python3

import turtle

pen = turtle.Turtle()
pen.getscreen().bgcolor('green')
pen.color('blue')
pen.speed(0)


def draw_square(size) -> None:
    if size < 1:
        return
    else:
        for _ in range(4):
            pen.forward(size*2)
            draw_square(size/2)
            pen.right(90)




draw_square(80)


turtle.done()





