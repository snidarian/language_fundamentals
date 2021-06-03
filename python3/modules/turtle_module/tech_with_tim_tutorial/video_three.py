#!/usr/bin/python3
# video three of python turtle tutorial
# url: https://www.youtube.com/watch?v=hPnZqWSRNZI


import turtle


turtle_object = turtle.Turtle()
turtle_object.speed(0)
turtle_object.width(5)


colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']


# the setheading values below correspond to standard compass headings (90 north) (270 south) etc
# sets turtle object facing up or north (90)
def up():
    turtle_object.setheading(90)
    turtle_object.forward(100)

def down():
    turtle_object.setheading(270)
    turtle_object.forward(100)

def left():
    turtle_object.setheading(180)
    turtle_object.forward(100)

def right():
    turtle_object.setheading(0)
    turtle_object.forward(100)


# listen for events - basically listen for events (keys pressed by user)
turtle.listen()

# first values are the functions to call and the string values are the names of the keys that triggers the calling of the functions
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'right')


 
turtle.mainloop()











