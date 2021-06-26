FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 260 )
        self.pendown()
        self.write(f"Level = {self.level}", move=False, align='center', font=FONT)

    def score_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level = {self.level}", move=False, align='center', font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write(f"Game Over", move=False, align='center', font=FONT)