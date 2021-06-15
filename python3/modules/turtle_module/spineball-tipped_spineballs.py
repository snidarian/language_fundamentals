#!/usr/bin/python3


import turtle as t
import math as m


pen = t.Turtle()
pen.speed(0)
pen.getscreen().bgcolor('blue')
pen.color('yellow')


def spineball(size) -> None:
    if size < 1:
        return
    else:
        for _ in range(4):
            pen.forward(size)
            for _ in range(10):
                pen.forward(size/2)
                for _ in range(10):
                    pen.color('red')
                    pen.forward(size/10)
                    for _ in range(10):
                        pen.color('cyan')
                        pen.forward(size/10)
                        pen.backward(size/10)
                        pen.left(36)
                    pen.color('red')
                    pen.backward(size/10)
                    pen.right(36)
                pen.color('orange')
                pen.backward(size/2)
                pen.right(36)
            pen.color('green')
            pen.backward(size)
            pen.color('yellow')
            pen.left(90)



spineball(200)




t.done()
















