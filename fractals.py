import turtle
import random

pen = turtle.Turtle()
pen.speed(100)
pen.color("blue")
pen.penup()

x = 0
y = 0
for n in range(110000):
    pen.goto(65 * x, 37 * y - 252) 
    pen.pendown()
    pen.dot(4, "green")
    pen.penup()
    r = random.random()
    r = r * 100
    xn = x
    yn = y
    if r < 1:
        x = 0
        y = 0.16 * yn
    elif r < 86:
        x = 0.85 * xn + 0.04 * yn
        y = -0.04 * xn + 0.85 * yn + 1.6
    elif r < 93:
        x = 0.20 * xn - 0.26 * yn
        y = 0.23 * xn + 0.22 * yn + 1.6
    else:
        x = -0.15 * xn + 0.28 * yn
        y = 0.26 * xn + 0.24 * yn + 0.44

turtle.Screen().exitonclick()