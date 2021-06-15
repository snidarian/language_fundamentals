#!/usr/bin/python3

import turtle

pen = turtle.Turtle()
pen.getscreen().bgcolor('blue')
pen.color('yellow')
pen.speed(0)


# -------------------------------------------------------
# definitions:
def draw_hexagon(size) -> None:
    if size < 1:
        return
    else:
        for _ in range(6):
            pen.forward(size*2)
            draw_triangle(size/2)
            pen.right(60)


def draw_triangle(size) -> None:
    if size < 1:
        return
    else:
        for _ in range(3):
            pen.forward(size*4)
            draw_hexagon(size/2)
            pen.right(120)


def main():
    draw_hexagon(50)

# --------------------------------------------------------------
# executions

main()


turtle.done()
