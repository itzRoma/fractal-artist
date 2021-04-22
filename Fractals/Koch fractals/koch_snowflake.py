
import turtle

win = turtle.Screen()
win.setup(1200, 700)
t = turtle.Turtle()
t.hideturtle()
t.up()
t.setposition(-300, 170)  # PERFECT
t.down()


itr = 4
length = 7
axiom = "F--F--F"
angle = 60
tempAx = ""
t.pensize(2)
# t.speed(0)
turtle.tracer(0)

translate = {"+": "+",
             "-": "-",
             "F": "F+F--F+F"}

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
