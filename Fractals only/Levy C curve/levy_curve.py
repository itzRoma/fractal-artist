
import turtle

win = turtle.Screen()
win.setup(1200, 700)
t = turtle.Turtle()
t.hideturtle()
t.up()
t.setposition(-250, 200)  # PERFECT
t.down()


itr = 13
length = 5.5
axiom = "F"
tempAx = ""
angle = 45
t.pensize(3)
turtle.tracer(0)
# t.speed(0)

translate = {"F": "+F--F+",
             "+": "+",
             "-": "-"}

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
