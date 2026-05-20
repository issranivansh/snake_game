from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from score import Scoreboard
screen=Screen()
scoreboard=Scoreboard()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on=True
snake=Snake()
food=Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
food.penup
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
        #collision 
    if snake.head.distance(food)<15:
        food.penup
        food.refresh()
        scoreboard.add()
        snake.add_new_body()
    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>285 or snake.head.ycor()<-285:
        scoreboard.reset()
        snake.reset()

for snakes in snake.turtles:
    if snakes == snake.head:
        pass
    elif snake.head.distance(snakes) < 10:
        scoreboard.reset()
        snake.reset()



















screen.exitonclick()
