#!/usr/bin/python3


import turtle

pen = turtle.Turtle()
pen.getscreen().bgcolor('black')
pen.color('white')
pen.speed(0)


def draw_hexagon(size) -> None:
    if size < 2:
        return
    else:
        for _ in range(6):
            pen.forward(size * 2)
            draw_hexagon(size/2)
            pen.right(60)




draw_hexagon(100)




turtle.done()



