from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.title("The Big Race")
user_bet = screen.textinput(title="Wager", prompt="Enter the color for the turtle you think will win: ")

# Create turtle instances with different colors and shapes for the purpose of creating a race
# Each turtle represents a participant

participants_position = [150, 100, 50, 0, -50, -100]
participants_color = ["red", "purple", "pink", "orange", "blue", "green"]
participants = []
all_turtles = []

race_on = False

for i in range(6):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(participants_color[i])
    turtle.penup()
    turtle.goto(x=-230, y=participants_position[i])
    participants.append(turtle)
    all_turtles.append(turtle)

if user_bet in participants_color:
    race_on = True

while race_on:

    
    for turtle in all_turtles:
        random_distance = random.randint(0, 15)
        turtle.forward(random_distance)

        # Check if any turtle has crossed the finish line
        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            race_on = False

screen.exitonclick() 
