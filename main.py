import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CAR_NUM = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
turtle = Player()
cars = []
for i in range(CAR_NUM):
    car = CarManager()
    cars.append(car)

screen.listen()
screen.onkey(turtle.turtle_move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.car_move()
        car.car_reset()
        if turtle.distance(car) < 20:
            game_is_on = False
            score.game_over()

    if turtle.ycor() > 280:
        score.score_up()
        turtle.reset()
        for car in cars:
            car.car_increase_speed()

screen.exitonclick()
