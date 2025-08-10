
from turtle import Turtle
ALIGNMENT = ("center")
FONT = ("Arial", 15, "normal")
class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score_data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_data.txt", mode="w") as data:
                data.write(f"{self.high_score}")


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


