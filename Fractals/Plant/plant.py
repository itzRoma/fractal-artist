
import turtle
from random import randint

win = turtle.Screen()
win.setup(1200, 704)
t = turtle.Turtle()
t.hideturtle()
t.up()
t.left(90)
t.setposition(0, -340)  # PERFECT
t.down()

itr = 7
length = 2
angle = 25
axiom = "X"
tempAx = ""
stack = []
turtle.tracer(0)

translate = {"+": "+",
             "-": "-",
             "[": "[",
             "]": "]",
             "X": "F-[[X]+X]+F[+FX]-X",
             "F": "FF"}

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
    elif ch == "F":
        t.forward(length)
    elif ch == "[":
        stack.append(t.xcor())
        stack.append(t.ycor())
        stack.append(t.heading())
    elif ch == "]":
        t.up()
        t.setheading(stack.pop())
        t.sety(stack.pop())
        t.setx(stack.pop())
        t.down()

turtle.done()
