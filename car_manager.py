from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.move_distance = 5
        self.make_cars()

    def make_cars(self):
        self.shape('square')
        self.turtlesize(stretch_len=2, stretch_wid=1)
        colour = random.choice(COLORS)
        self.penup()
        self.color(colour)
        self.setheading(180)
        random_y = random.randint(-250, 270)
        random_x = random.randint(-270, 300)
        self.goto(random_x, random_y)

    def car_increase_speed(self):
        self.move_distance += 5

    def car_move(self):
        self.forward(self.move_distance)

    def car_reset(self):
        if self.xcor() < -320:
            random_y = random.randint(-250, 270)
            self.goto(320, random_y)
