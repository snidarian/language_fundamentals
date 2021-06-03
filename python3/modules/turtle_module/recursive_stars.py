#!/usr/bin/python3

import turtle
import random as r
import math as m
import time
import argparse

parser = argparse.ArgumentParser(description="Generates recursively drawn isolateral star structure")

args = parser.add_argument("complexity", help="Select complexity with integer", type=int, default=3)

args = parser.parse_args()


pen = turtle.Turtle()
pen.getscreen().bgcolor('teal')
pen.color('red')
pen.speed(0)

def draw_star(scale) -> None:
    for _ in range(5):
        pen.forward(50 * scale)
        pen.left(144)
        if scale > 1:
            draw_star(scale -1)
        else:
            continue


# Calling the function with a higher scale value will create greater complexity and greater run time
# change the value of the parameter supplied to this function to vary the complexity
draw_star(args.complexity)





turtle.done()



