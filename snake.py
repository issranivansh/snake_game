from turtle import Turtle
MOVE_DISTTANCE=20
class Snake:
    def __init__(self):
        self.turtles=[]
        self.create_snake()
        self.move()
        self.head=self.turtles[0]
        self.right()
        self.left()
        self.up()
        self.down()
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def create_snake(self):
        for i in range(3):
            new_turtle=Turtle(shape="square")
            new_turtle.pu()
            new_turtle.color("white")
            new_turtle.goto(-i*20,0)
            self.turtles.append(new_turtle)
    def move(self):
        for seg_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[seg_num - 1].xcor()
            new_y = self.turtles[seg_num - 1].ycor()
            self.turtles[seg_num].goto(new_x, new_y)

        self.turtles[0].forward(MOVE_DISTTANCE)
    def add_new_body(self):
        last_segment = self.turtles[-1]  # get last segment
    
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
    
        # place new segment at last segment position
        new_turtle.goto(last_segment.xcor(), last_segment.ycor())
    
        self.turtles.append(new_turtle)
    
        
