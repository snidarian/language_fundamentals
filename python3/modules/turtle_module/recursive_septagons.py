#!/usr/bin/python3

import turtle

pen = turtle.Turtle()
pen.getscreen().bgcolor('blue')
pen.color('black')
pen.speed(0)

def draw_septagons(size) -> None:
    if size < 2:
        return
    else:
        for _ in range(7):
            pen.forward(size * 3)
            draw_septagons(size/2)
            pen.left(51.42857)




draw_septagons(25)




turtle.done()
