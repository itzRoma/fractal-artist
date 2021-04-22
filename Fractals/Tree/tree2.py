
import turtle
from random import randint

win = turtle.Screen()
win.setup(1200, 704)
t = turtle.Turtle()
t.hideturtle()
t.up()
t.left(90)
t.setposition(0, -390)  # PERFECT
t.down()


itr = 12
length = 11
angle = 16
axiom = "22220"
tempAx = ""
stack = []
thick = 16
t.pensize(thick)
turtle.tracer(0)

translate = {"1": "21",
             "0": "1[-20]+20"}

for i in range(itr):
    for ch in axiom:
        if ch in translate:
            tempAx += translate[ch]
        else:
            tempAx += ch
    axiom = tempAx
    tempAx = ""

for ch in axiom:
    if ch == "+":
        t.right(angle - randint(-13, 13))
    elif ch == "-":
        t.left(angle - randint(-13, 13))
    elif ch == "1" or ch == "2":
        if randint(0, 10) > 4:
            t.forward(length)
    elif ch == "0":
        stack.append(t.pensize())
        t.pensize(4)
        r = randint(0, 10)
        if r < 3:
            t.pencolor("#009900")
        elif r > 6:
            t.pencolor("#667900")
        else:
            t.pencolor("#20BB00")
        t.forward(length - 2)
        t.pensize(stack.pop())
        t.pencolor("black")
    elif ch == "[":
        thick = thick * 0.75
        t.pensize(thick)
        stack.append(thick)
        stack.append(t.xcor())
        stack.append(t.ycor())
        stack.append(t.heading())
    elif ch == "]":
        t.up()
        t.setheading(stack.pop())
        t.sety(stack.pop())
        t.setx(stack.pop())
        thick = stack.pop()
        t.pensize(thick)
        t.down()

turtle.done()
