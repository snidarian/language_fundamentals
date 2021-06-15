#!/usr/bin/python3
# generating a symbol for linfintec

import turtle as t
import math as m
import numpy as np
import random as r


# color combination set in hex
# background - faintly greened steel grey - #c3d2c1
# color1 - #77721d - dark gold
# color2 - #30771d - dark green
# color3 - #dedf58 - light yellow
# color4 - #ce58df - magenta
# color5 - #58df9a - tealish
# color6 - #4cbb17 - kelly green


pen = t.Turtle()
pen.getscreen().bgcolor('#202020')
pen.color('#77721d')
pen.speed(0)

# list from which function randomly selects pen colors
color_set = [ '#77721d', '#30771d', '#dedf58', '#4cbb17']


def draw_hexagon(size) -> None:
    
    if size < 5:
        return
    else:
        for _ in range(6):
            pen.color(r.choice(color_set))
            pen.forward(size/2)
            draw_triangle(size/2)
            pen.forward(size/2)
            pen.right(60)


def draw_triangle(size) -> None:
    
    if size < 5:
        return
    else:
        for _ in range(3):
            pen.color(r.choice(color_set))
            pen.forward(size/2)
            draw_hexagon(size/2)
            pen.forward(size/2)
            pen.right(120)



draw_hexagon(100)




t.done()



