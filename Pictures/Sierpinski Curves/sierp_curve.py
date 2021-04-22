
import turtle

win = turtle.Screen()
win.setup(1200, 704)
t = turtle.Turtle()
t.hideturtle()
t.up()
# t.left(90)
t.setposition(0, 340)  # PERFECT
t.down()

itr = 5
length = 6.3
axiom = "F--XF--F--XF"
tempAx = ""
angle = 45
turtle.tracer(0)
t.pensize(2)

translate = {"F": "F",
             "G": "G",
             "+": "+",
             "-": "-",
             "X": "XF+G+XF--F--XF+G+X"}

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
