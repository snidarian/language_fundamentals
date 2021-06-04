#!/usr/bin/python3

import turtle


pen = turtle.Turtle()
pen.getscreen().bgcolor('black')
pen.speed(0)


# every successive recursive function call reverses the direction of the triangles using "reversed" boolean variable
def draw_triangle(size: float, reversed: bool) -> None:
    if reversed == True:
        pen.color('blue')
        reversed = False
    elif reversed == False:
        pen.color('red')
        reversed = True
    if size < 1:
        return
    else:
        for _ in range(3):
            pen.forward(size*2)
            draw_triangle((size/1.9), reversed)
            if reversed == False:
                pen.right(120)
            elif reversed == True:
                pen.left(120)


def main():
    draw_triangle(120, True)


main()


turtle.done()







