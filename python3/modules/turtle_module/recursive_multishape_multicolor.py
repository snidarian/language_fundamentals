#!/usr/bin/python3

import turtle


pen = turtle.Turtle()
pen.getscreen().bgcolor('blue')
pen.color('orange')
pen.speed(0)



def draw_many_shapes(size) -> None:
    if size >= 10:
        pen.color('green')
        for _ in range(6):
            pen.forward(size*3)
            draw_many_shapes(size/2)
            pen.left(60)
    elif size >= 5:
        pen.color('yellow')
        for _ in range(4):
            pen.forward(size*4)
            draw_many_shapes(size/2)
            pen.left(90)
    elif size >= 2:
        pen.color('red')
        for _ in range(3):
            pen.forward(size*3)
            draw_many_shapes(size/2)
            pen.left(120)
    elif size < 1:
        return



def main():
    draw_many_shapes(50)



main()


turtle.done()











