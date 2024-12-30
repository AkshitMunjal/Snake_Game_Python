from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segment = []
        self.cord = [(0, 0), (-20, 0), (-40, 0)]
        self.make_snake()
        self.head = self.segment[0]

    def make_snake(self):
        for position in self.cord:
            self.add_segment(position)

    def move_snake(self):
        for item in range(len(self.segment) - 1, 0, -1):
            x_cord = self.segment[item - 1].xcor()
            y_cord = self.segment[item - 1].ycor()
            self.segment[item].goto(x_cord, y_cord)

        self.head.forward(MOVE_DISTANCE)

    def grow_snake(self):
        self.add_segment(self.segment[-1].position())


    def add_segment(self,position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segment.append(tim)

    def up_key(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down_key(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left_key(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right_key(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset_snake(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.make_snake()
        self.head = self.segment[0]
