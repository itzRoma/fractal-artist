
import turtle

win = turtle.Screen()
win.setup(1200, 704)
t = turtle.Turtle()
t.hideturtle()
t.up()
# t.left(90)
t.setposition(-400, -340)  # PERFECT
t.down()


itr = 7
length = 6.2
axiom = "F-G-G"
tempAx = ""
angle = 120
t.pensize(2)
turtle.tracer(0)

translate = {"F": "F-G+F+G-F",
             "G": "GG",
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
        t.right(angle)
    elif ch == "-":
        t.left(angle)

turtle.done()
