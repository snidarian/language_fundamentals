#!/usr/bin/python3


import turtle


pen = turtle.Turtle()
pen.getscreen().bgcolor('red')
pen.speed(0)
pen.color('black')


def draw_pentagon(size) -> None:
    if size < 1:
        return
    else:
        for _ in range(5):
            pen.forward(size * 2)
            draw_pentagon(size/2)
            pen.right(72)




draw_pentagon(50)


turtle.done()









