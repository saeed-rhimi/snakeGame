from turtle import Turtle


class Food(Turtle):
    import random

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.move()

    def generate_random_number(self):
        return round(self.random.uniform(-290, 290) / 20) * 20

    def move(self):
        self.goto(self.generate_random_number(), self.generate_random_number())

    def clear(self):
        self.hideturtle()