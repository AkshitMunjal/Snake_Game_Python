from turtle import Turtle

class Score:

    def __init__(self):
        self.current_score = 0
        with open("data.txt") as data:
            self.high_current_score = int(data.read())

        self.score = Turtle()
        self.score.hideturtle()
        self.score_appear()


    def score_appear(self):
        self.score.color("white")
        self.score.penup()
        self.score.goto(-190, 270)
        self.update_score()

    def update_score(self):
        self.score.clear()
        self.score.write(f"Score: {self.current_score}        High Score: {self.high_current_score}", align="left", font=("Arial", 20, "normal"))


    def reset(self):
        if self.current_score > self.high_current_score:
            self.high_current_score = self.current_score
            with open("data.txt","w") as data:
                data.write(f"{self.high_current_score}")

        self.current_score = 0
        self.update_score()


