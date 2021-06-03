#!/usr/bin/python3
# recursive star draw function. 
# Function calls itself recursively but doesnt draw stars within stars within stars

import turtle
import random as r

pen = turtle.Turtle()
turtle.bgcolor('blue')
pen.color('yellow')
pen.width(1)
pen.speed(7)
pen.setheading(180)


def draw_star(scale) -> None:
    size = (scale * 100)
    for _ in range(5):
        pen.forward(size)
        pen.left(144)
    return (scale + 1)



draw_star(draw_star(draw_star(draw_star(draw_star(draw_star(draw_star(draw_star(1))))))))
    


# keeps windo open after drawing has finished
turtle.done()
