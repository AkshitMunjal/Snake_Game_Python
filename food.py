from turtle import Turtle
import random

class Food:

    def __init__(self):
        self.dot = Turtle("circle")
        self.make_food()


    def make_food(self):
        self.dot.color("Blue")
        self.dot.shapesize(0.5,0.5)
        self.dot.penup()
        self.dot.speed("fastest")
        self.rand_location()


    def rand_location(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.dot.goto(rand_x, rand_y)
