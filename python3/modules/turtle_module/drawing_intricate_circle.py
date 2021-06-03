#!/usr/bin/python3
# this program draws a intricate circle

import turtle as turtle

pen = turtle.Turtle()
pen.speed(0)
pen.color('red')
turtle.bgcolor('blue')


def draw_star() -> None:
    for _ in range(185):
        pen.forward(600)
        pen.left(179)
        
    


while True:
    draw_star()
    pen.clear()
    

# turtle.done() keeps the gui open after the images has been drawn
turtle.done()










