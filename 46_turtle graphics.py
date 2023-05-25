from turtle import *
t=Turtle()
wn=Screen()
wn.title("My First Graphics")
wn.bgcolor("Black")
t.shape("arrow")
t.color("red","green")
t.hideturtle()
t.speed(1)

t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
done()
 
