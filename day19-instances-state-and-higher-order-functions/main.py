#My completed version 8/1/25
from turtle import Turtle, Screen


lil_turt = Turtle()
screen = Screen()

def move_forwards():
    lil_turt.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()