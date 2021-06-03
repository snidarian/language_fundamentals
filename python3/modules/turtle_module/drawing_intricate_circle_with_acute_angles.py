#!/usr/bin/python3
# this program draws a intricate circle

import turtle as turtle

pen = turtle.Turtle()
pen.speed(0)
pen.color('red')
turtle.bgcolor('blue')


def draw_intricate_circle() -> None:
    for _ in range(185):
        pen.forward(600)
        pen.left(179)
        
    


while True:
    draw_intricate_circle()
    pen.clear()
    

# turtle.done() keeps the gui open after the images has been drawn
turtle.done()










