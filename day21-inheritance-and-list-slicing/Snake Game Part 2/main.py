#My completed version 8/3/25
from turtle import Screen
from snake_class import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


slither = Snake()
food = Food()
points = Scoreboard()

screen.listen()
screen.onkey(slither.up, "Up")
screen.onkey(slither.down, "Down")
screen.onkey(slither.left, "Left")
screen.onkey(slither.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.09)
    slither.move()

    #Detec collision with food.
    if slither.head.distance(food) < 15:
        food.refresh()
        slither.extend()
        points.increase_score()

    #Detect collision with wall.
    if slither.head.xcor() > 280 or slither.head.xcor() < -280 or slither.head.ycor() > 280 or slither.head.ycor() < -280:
        points.game_over()
        game_on = False

    #Detect collision with any part in the tail.
    for snake_part in slither.snake_parts[1:]:

        if slither.head.distance(snake_part) < 10:
            game_on = False
            points.game_over()


screen.exitonclick()