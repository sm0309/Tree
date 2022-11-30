import turtle
from turtle import *
bgcolor('black')
pensize(2)
left(90)
speed(200)
color('green')
shape('turtle')

def tree_speed(i):
    if i<10:
        return
    else:
        forward(i)
        circle(i*2)
        backward(30)
        left(30)
        right(90)
        forward(90)
        color('orange')
        forward(60)
        right(30)
        tree_speed(3*i/4)
        backward(45)
        tree_speed(3*i/4)
        left(30)
        right(60)
        forward(30)

tree_speed(100)
done()