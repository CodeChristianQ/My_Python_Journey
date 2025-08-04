#My completed version 8/2/25
from turtle import Screen
from snake_class import Snake
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


slither = Snake()

screen.listen()
screen.onkey(slither.up, "Up")
screen.onkey(slither.down, "Down")
screen.onkey(slither.left, "Left")
screen.onkey(slither.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    slither.move()





screen.exitonclick()