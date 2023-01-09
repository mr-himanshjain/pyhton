import turtle
from turtle import *
screen = turtle.Screen()
t = turtle.Turtle()
speed(3)

t.penup()
t.goto(-200,125)
t.pendown()

t.color("orange")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(64)
t.right(90)
t.forward(400)
t.right(90)
t.forward(64)
t.end_fill()
t.left(180)
t.forward(128)
t.color("green")
t.begin_fill()
t.left(90)
t.forward(400)
t.right(90)
t.forward(64)
t.right(90)
t.forward(400)
t.right(90)
t.forward(64)
t.end_fill()
t.right(90)
t.forward(200)
t.color("blue")
t.begin_fill()
t.circle(32)
for i in range(1):
    t.forward(10)
    t.left(90)
    t.forward(40)
    t.left(180)
    t.forward(40)
    t.left(120)
    for i in range(1,14):
        t.forward(15)
        t.left(90)
        t.forward(40)
        t.left(180)
        t.forward(40)
        t.left(116.5)





