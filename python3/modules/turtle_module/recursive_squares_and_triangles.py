#!/usr/bin/python3

import turtle

pen = turtle.Turtle()
pen.getscreen().bgcolor('red')
pen.color('blue')
pen.speed(0)


# -------------------------------------------------------
# definitions:
def draw_square(size) -> None:
    if size < 1:
        return
    else:
        for _ in range(4):
            pen.forward(size*2)
            draw_triangle(size/2)
            pen.right(90)


def draw_triangle(size) -> None:
    if size < 1:
        return
    else:
        for _ in range(3):
            pen.forward(size*2)
            draw_square(size/2)
            pen.right(120)


def main():
    draw_square(80)

# --------------------------------------------------------------
# executions

main()


turtle.done()
