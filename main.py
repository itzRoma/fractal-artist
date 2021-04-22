import turtle
import tkinter as tk
from tkinter import ttk
from src import *
from random import randint
from tkinter import messagebox
from pyautogui import size

# ---------------------------------------------------Window settings----------------------------------------------------

win = tk.Tk()  # Create window

win_width, win_height = 1594, 704  # Window size settings
width, height = size()             # Window size settings
left = (width - win_width) / 2     # Window size settings
top = (height - win_height) / 2    # Window size settings

win.title("Fractal artist")
win.geometry(f"{win_width}x{win_height}+{int(left)}+{int(top)}")
bg_color = "#140f19"
win.config(bg=bg_color)
icon = tk.PhotoImage(file="icon.png")
win.iconphoto(False, icon)
font = "Comic Sans MS"

# -----------------------------------------------------Main title-------------------------------------------------------


def hor_line(text, bg, fg, font, width, row, column, columnspan, stick):
    tk.Label(win, text=text, bg=bg,
             fg=fg, font=font, width=width).grid(row=row, column=column, columnspan=columnspan, stick=stick)


hor_line("----------------", bg_color, "#fff", (font, 30, "bold"), 16, 0, 0, 2, "we")

title = tk.Label(win, text="Fractal artist",
                 bg=bg_color,
                 fg="#fff",
                 font=(font, 30, "bold"),
                 width=16).grid(row=1, column=0, columnspan=2, stick="we")

hor_line("----------------", bg_color, "#fff", (font, 30, "bold"), 16, 2, 0, 2, "we")

# ----------------------------------------------Buttons "Draw" and "Clear"----------------------------------------------


def draw_shape():
    shape_to_draw = shape_combo.current()
    shape_color = color_combo.current()
    feather.color(colors[shape_color])

    axiom = axioms[shapes[shape_to_draw]]
    angle = angles[shapes[shape_to_draw]]
    translate = translations[shapes[shape_to_draw]]
    iteration = iterations[shapes[shape_to_draw]]
    length = lengths[shapes[shape_to_draw]]
    pensize = pensizes[shapes[shape_to_draw]]

    field.tracer(0)
    feather.clear()
    feather.setposition(0, 0)
    feather.setheading(0)
    feather.setposition(start_position[shapes[shape_to_draw]])
    if shape_to_draw in (4, 5, 11):
        feather.left(90)
    feather.clear()
    feather.pensize(pensize)
    stack = []
    tempAx = ""
    thick = 16

    for i in range(iteration):
        for ch in axiom:
            if ch in translate:
                tempAx += translate[ch]
            else:
                tempAx += ch
        axiom = tempAx
        tempAx = ""

    for ch in axiom:
        if shape_to_draw in (1, 2, 6, 7, 8):
            if ch == "F" or ch == "G":
                feather.forward(length)
            elif ch == "+":
                feather.left(angle)
            elif ch == "-":
                feather.right(angle)
        elif shape_to_draw in (0, 3, 4, 5, 9, 10, 11):
            if ch in ("F", "G", "1", "0") and shape_to_draw != 11:
                feather.forward(length)
            if ch == "C":
                feather.begin_fill()
                for i in range(4):
                    feather.forward(length)
                    feather.left(angle)
                feather.end_fill()
            elif ch == "f":
                feather.up()
                feather.forward(length)
                feather.down()
            elif ch == "+" and shape_to_draw not in (4, 11):
                feather.right(angle)
            elif ch == "-" and shape_to_draw not in (4, 11):
                feather.left(angle)
            elif ch == "+" and shape_to_draw in (4, 11):
                feather.right(angle - randint(-13, 13))
            elif ch == "-" and shape_to_draw in (4, 11):
                feather.left(angle - randint(-13, 13))
            elif ch == "[" and shape_to_draw != 11:
                stack.append(feather.xcor())
                stack.append(feather.ycor())
                stack.append(feather.heading())
            elif ch == "]" and shape_to_draw != 11:
                feather.up()
                feather.setheading(stack.pop())
                feather.sety(stack.pop())
                feather.setx(stack.pop())
                feather.down()
            elif ch in ("1", "2") and shape_to_draw == 11:
                if randint(0, 10) > 4:
                    feather.forward(length)
            elif ch == "0" and shape_to_draw == 11:
                stack.append(feather.pensize())
                feather.pensize(4)
                r = randint(0, 10)
                if r < 3:
                    feather.pencolor("#009900")
                elif r > 6:
                    feather.pencolor("#667900")
                else:
                    feather.pencolor("#20BB00")
                feather.forward(length - 2)
                feather.pensize(stack.pop())
                feather.pencolor(colors[shape_color])
            elif ch == "[" and shape_to_draw == 11:
                thick = thick * 0.75
                feather.pensize(thick)
                stack.append(thick)
                stack.append(feather.xcor())
                stack.append(feather.ycor())
                stack.append(feather.heading())
            elif ch == "]" and shape_to_draw == 11:
                feather.up()
                feather.setheading(stack.pop())
                feather.sety(stack.pop())
                feather.setx(stack.pop())
                thick = stack.pop()
                feather.pensize(thick)
                feather.down()


def field_clear():
    feather.up()
    feather.home()
    feather.down()
    feather.clear()


def create_button(text, bg, fg, font, width, borderwidth, cursor, active_bg, com, row, column):
    tk.Button(win, text=text, bg=bg, fg=fg, font=font, width=width,
              borderwidth=borderwidth, cursor=cursor,
              activebackground=active_bg, command=com).grid(row=row, column=column)


hor_line("----------------", bg_color, "#fff", (font, 30, "bold"), 16, 8, 0, 2, "we")
create_button("Draw", bg_color, "#fff", (font, 20, "bold"), 8, 0, "spraycan", bg_color, draw_shape, 9, 0)
create_button("Clear", bg_color, "#fff", (font, 20, "bold"), 8, 0, "exchange", bg_color, field_clear, 9, 1)
hor_line("----------------", bg_color, "#fff", (font, 30, "bold"), 16, 10, 0, 2, "we")

# --------------------------------------------------------Labels--------------------------------------------------------


def create_title(text, bg, fg, font, row, column):
    tk.Label(win, text=text, bg=bg, fg=fg, font=font).grid(row=row, column=column)


def dot_line(text, bg, fg, font, width, row, column, columnspan, stick):
    tk.Label(win, text=text, bg=bg,
             fg=fg, font=font, width=width).grid(row=row, column=column, columnspan=columnspan, stick=stick)


create_title("Choose a shape", bg_color, "#fff", (font, 14, "bold"), 3, 0)
dot_line("<•><•><•><•><•>", bg_color, "#fff", (font, 30, "bold"), 16, 4, 0, 2, "we")
create_title("Choose a shape color", bg_color, "#fff", (font, 14, "bold"), 5, 0)
dot_line("<•><•><•><•><•>", bg_color, "#fff", (font, 30, "bold"), 16, 6, 0, 2, "we")
create_title("Choose a\nbackground color", bg_color, "#fff", (font, 14, "bold"), 7, 0)

# ------------------------------------------------------ComboBoxes------------------------------------------------------


def selected_bg_color(event):
    background_color = bg_color_combo.current()
    canvas.config(bg=colors[background_color])


# Define CB

shape_combo = ttk.Combobox(win, value=shapes)
shape_combo.current(0)
shape_combo["state"] = "readonly"
shape_combo.bind("<<ComboboxSelected>>")
shape_combo.grid(row=3, column=1)

color_combo = ttk.Combobox(win, value=colors)
color_combo.current(0)
color_combo["state"] = "readonly"
color_combo.bind("<<ComboboxSelected>>")
color_combo.grid(row=5, column=1)

bg_color_combo = ttk.Combobox(win, value=colors)
bg_color_combo.current(1)
bg_color_combo["state"] = "readonly"
bg_color_combo.bind("<<ComboboxSelected>>", selected_bg_color)
bg_color_combo.grid(row=7, column=1)

# --------------------------------------------------------Canvas--------------------------------------------------------

canvas = tk.Canvas(win, width=1200, height=700)
canvas.grid(row=0, column=3, rowspan=11)

# --------------------------------------------------------Turtle--------------------------------------------------------

field = turtle.TurtleScreen(canvas)
feather = turtle.RawTurtle(field)
feather.hideturtle()

# --------------------------------------------------------Message-------------------------------------------------------

messagebox.showinfo("Recommend display settings", "Perfect display resolution: 1920x1080!\n"
                                                  "Perfect display scale: 100%!")

# -------------------------------------------------------Main loop------------------------------------------------------

win.mainloop()
