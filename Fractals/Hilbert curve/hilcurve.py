
import turtle

win = turtle.Screen()
win.setup(1200, 700)
t = turtle.Turtle()
t.hideturtle()
t.up()
t.setposition(-330, -310)  # PERFECT
t.down()


itr = 6
length = 10
axiom = "A"
angle = 90
tempAx = ""
t.speed(0)
t.pensize(3)

translate = {"+": "+",
             "-": "-",
             "F": "F",
             "A": "+BF-AFA-FB+",
             "B": "-AF+BFB+FA-"}

for i in range(itr):
    for ch in axiom:
        tempAx += translate[ch]
    axiom = tempAx
    tempAx = ""

for ch in axiom:
    if ch == "F":
        t.forward(length)
    elif ch == "+":
        t.left(angle)
    elif ch == "-":
        t.right(angle)

turtle.done()
