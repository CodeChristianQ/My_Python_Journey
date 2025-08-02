#My completed version 07/30/25
import turtle
#How do we remember how to use modules or packages? We don't. We reference Documentation when available.
#Example: https://docs.python.org/3/library/turtle.html
#We often use resources like https://stackoverflow.com/questions of Google.
from turtle import Turtle, Screen
import random
turt = Turtle()
turtle.colormode(255)
#We can change the shape of jimmy by using .shape() with the shape string in the parenthesis.
turt.shape("turtle")
#We can change the color by using .color() with the color string in the parenthesis.
#This method accepts input for color as in pencolor() which gets it's color as s Tk color specification string.
#What is Tk? tkinter aka tk interface, which is used to create a GUI
turt.color("green")
#We can also make jimmy move or face a specific direction by using.

# turt.right(90)
# turt.forward(140)

#Challenge 1 - make jimmy draw a square.

# for _ in range(4):
#     turt.right(90)
#     turt.forward(140)

#Challenge 2 - draw a dashed line.

import turtle as turtle_mod
from turtle import Screen
import random
turtle_mod.colormode(255)
hirst = turtle_mod.Turtle()
hirst.shape("turtle")
hirst.penup()
hirst.hideturtle()
hirst.speed("fastest")

color_list = [(213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40),
 (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222),
 (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203),
 (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155), (238, 157, 212), (86, 77, 208), (86, 225, 235),
 (250, 8, 14), (242, 166, 157), (177, 180, 224), (36, 243, 159), (6, 81, 115), (11, 55, 248)]

hirst.setheading(230)
hirst.forward(250)
hirst.setheading(0)
dot_count = 100

for dots in range(1, dot_count + 1):
    hirst.dot(20, random.choice(color_list))
    hirst.forward(50)
    if dots % 10 == 0:
        hirst.setheading(90)
        hirst.forward(50)
        hirst.setheading(180)
        hirst.forward(500)
        hirst.setheading(0)

# for _ in range(15):
#     turt.forward(10)
#     turt.penup()
#     turt.forward(10)
#     turt.pendown()

#Challenge 3 - draw a shape in a shape in a shape all while changing each lines color.
colors = ["red", "orange", "green", "blue", "purple", "black", "brown", "aqua"]

def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        turt.pensize(5)
        turt.speed("fastest")
        turt.forward(50)
        turt.right(angle)

for shape_side in range(3, 33):
    turt.color(random.choice(colors))
    draw_shape(shape_side)

#Challenge 4 - get the turtle to do a random walk.

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# direction = [0, 90, 180, 270]
#
# for _ in range(500):
#     turt.speed("fastest")
#     turt.pensize(30)
#     turt.forward(100)
#     turt.setheading(random.choice(direction))
#     turt.color(random_color())

#Challenge 5 - draw a spirograph

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turt.speed("fastest")
        turt.pensize(15)
        turt.color(random_color())
        turt.circle(250)
        turt.setheading(turt.heading() + 10)

draw_spirograph(10)


screen = Screen()
screen.exitonclick()