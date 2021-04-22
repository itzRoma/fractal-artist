
import turtle

win = turtle.Screen()
win.setup(1200, 700)
t = turtle.Turtle()
t.hideturtle()
t.up()
t.setposition(270, 110)  # PERFECT
t.down()


itr = 12
length = 10
axiom = "FX"
tempAx = ""
angle = 90
# t.speed(0)
turtle.tracer(0)
t.pensize(3)

translate = {"F": "F",
             "X": "X+YF+",
             "Y": "-FX-Y",
             "-": "-",
             "+": "+"}

for i in range(itr):
    for ch in axiom:
        tempAx += translate[ch]
    axiom = tempAx
    tempAx = ""

for ch in axiom:
    if ch == "F":
        t.forward(length)
    elif ch == "+":
        t.right(angle)
    elif ch == "-":
        t.left(angle)

turtle.done()
