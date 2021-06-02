#!/usr/bin/python3
# video url - https://www.youtube.com/watch?v=p7CiFhiTdvY

import turtle

# create turtle object
turtle_object = turtle.Turtle()


while True:
    # color of object
    turtle_object.color('teal') # it will recognize any basic color names like green, orange, purple, yellow, teal, maroon
    # size of line drawn under object
    turtle_object.pensize(1)
    # shape of the object
    turtle_object.shape('arrow')
    
    # makes object move forward
    turtle_object.forward(20)
    
    # turns object by X degrees left
    turtle_object.left(10)
    # turns object by x degrees right
    # turtle_object.right

    # lifts line-drawing pen up from turtle object (makes line invisible)
    turtle_object.penup()

    # puts line-drawing pen down from turtle object (makes line invisible)
    turtle_object.pendown()


# you can create multiple turtle objects
# turtle_object0 = turtle.Turtle()


































