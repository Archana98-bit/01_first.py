import turtle
import time
turtle.shape("turtle")
turtle.color("red")
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.pensize(5)

turtle.left(140)
turtle.forward(224)
turtle.circle(-112, 200)
turtle.setheading(60)
turtle.circle(-112, 200)
turtle.forward(224)
turtle.end_fill()

turtle.penup()
turtle.goto(-120, -180)
turtle.pendown()
turtle.write("I Love You!", font=("Arial", 36, "normal"))

t= turtle.Turtle()
colors=["purple", "pink", "maroon", "magenta", "light slate blue", "violet", "black"]

for color in colors:
    t.screen.bgcolor(color)
    time.sleep(1)

turtle.done()

