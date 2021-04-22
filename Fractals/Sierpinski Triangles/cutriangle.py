
import turtle

win = turtle.Screen()
win.setup(1200, 704)
t = turtle.Turtle()
t.hideturtle()
t.up()
# t.left(90)
t.setposition(-400, -340)  # PERFECT
t.down()


itr = 8
length = 3
axiom = "F-G-F"
tempAx = ""
angle = 60
t.pensize(2)
turtle.tracer(0)

translate = {"F": "G-F-G",
             "G": "F+G+F",
             "+": "+",
             "-": "-"}

for i in range(itr):
    for ch in axiom:
        tempAx += translate[ch]
    axiom = tempAx
    tempAx = ""

for ch in axiom:
    if ch == "F" or ch == "G":
        t.forward(length)
    elif ch == "+":
        t.left(angle)
    elif ch == "-":
        t.right(angle)

turtle.done()
