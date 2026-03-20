from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()
    def add(self):
        self.score+=1
        self.clear()
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()
    def end(self):
        self.penup()
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Arial",40,"normal"))
