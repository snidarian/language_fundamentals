#!/usr/bin/python3

import turtle
import random as r
import time

pen = turtle.Turtle()
pen.speed(7)
color_list = ['red', 'blue', 'green', 'yellow', 'cyan', 'black', 'white', 'teal', 'maroon', 'pink']
pen.getscreen().bgcolor(r.choice(color_list))

def draw_star(x_value: int, y_value: int, scale: int, outline_color: str, fill_color: str) -> None:
    pen.penup()
    pen.setpos(x_value, y_value)
    pen.pendown()
    pen.color(outline_color, fill_color)
    pen.begin_fill()
    # dichotomize star heading
    if (r.randint(0, 1)):
        for _ in range(5):
            pen.forward(scale * 100)
            pen.left(144)
    else:
        for _ in range(5):
            pen.forward(scale * 100)
            pen.right(144)
    pen.end_fill()


while True:
    randomx = r.randint(-500, 500)
    randomy = r.randint(-300, 300)
    random_outline_color = r.choice(color_list)
    random_fill_color = r.choice(color_list)
    random_scale = r.randint(1, 3)
    draw_star(randomx, randomy, random_scale, random_outline_color, random_fill_color)
    time.sleep(.5)
