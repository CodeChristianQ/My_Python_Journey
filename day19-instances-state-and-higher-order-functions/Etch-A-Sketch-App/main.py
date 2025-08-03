#My completed version 8/1/25
from turtle import Turtle, Screen


lil_turt = Turtle()
screen = Screen()

def move_forwards():
    lil_turt.forward(10)
def rotate_right():
    lil_turt.right(10)
def rotate_left():
    lil_turt.left(10)
def move_backwards():
    lil_turt.backward(10)
def clear():
    lil_turt.clear()
    lil_turt.penup()
    lil_turt.home()
    lil_turt.pendown()

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=rotate_left, key="a")
screen.onkey(fun=rotate_right, key="d")
screen.onkey(clear, "c")

screen.exitonclick()