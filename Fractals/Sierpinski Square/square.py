
import turtle

win = turtle.Screen()
win.setup(1200, 704)
t = turtle.Turtle()
t.hideturtle()
t.up()
t.setposition(-335, -320)  # PERFECT
t.down()


itr = 4
length = 8
axiom = "C"
tempAx = ""
angle = 90
t.pensize(1)
t.fillcolor("black")
turtle.tracer(0)

translate = {"+": "+",
             "-": "-",
             "C": "CfCfC-f+C-f+C--f--C--f--C+f-C+f-",
             "f": "fff"}

for i in range(itr):
    for ch in axiom:
        tempAx += translate[ch]
    axiom = tempAx
    tempAx = ""

for ch in axiom:
    if ch == "C":
        t.begin_fill()
        for i in range(4):
            t.forward(length)
            t.left(angle)
        t.end_fill()
    elif ch == "f":
        t.up()
        t.forward(length)
        t.down()
    elif ch == "+":
        t.right(angle)
    elif ch == "-":
        t.left(angle)

turtle.done()
