
import turtle

win = turtle.Screen()
win.setup(1200, 704)
t = turtle.Turtle()
t.hideturtle()
t.up()
t.left(90)
t.setposition(0, -340)  # PERFECT
t.down()


itr = 8
length = 2.9
axiom = "0"
tempAx = ""
angle = 45
stack = []
t.pensize(2)
turtle.tracer(0)

translate = {"1": "11",
             "0": "1[-0]+0"}

for i in range(itr):
    for ch in axiom:
        if ch in translate:
            tempAx += translate[ch]
        else:
            tempAx += ch
    axiom = tempAx
    tempAx = ""

for ch in axiom:
    if ch == "1" or ch == "0":
        t.forward(length)
    elif ch == "+":
        t.right(angle)
    elif ch == "-":
        t.left(angle)
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
