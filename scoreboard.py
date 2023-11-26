from turtle import Turtle


class Scoreboard(Turtle):
    SCORE = 0
    POSITION = (0, 280)
    ALIGNMENT = "center"
    FONT = ('Courier', 15, 'normal')
    HIGH_SCORE = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(self.POSITION)
        self.read_highscore()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.SCORE}  HighScore: {self.HIGH_SCORE}", align=self.ALIGNMENT, font=self.FONT)

    def increase_score(self):
        self.SCORE += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.home()
        self.write(f"You lost! You're Final Score is: {self.SCORE} \n         Highscore is: {self.HIGH_SCORE} ", align=self.ALIGNMENT,font=self.FONT)

    def update_highscore(self):
        if self.SCORE > self.HIGH_SCORE:
            self.HIGH_SCORE = self.SCORE
            with open("data.txt", mode="w") as file:
                file.write(str(self.HIGH_SCORE))

    def read_highscore(self):
        with open("data.txt", mode="r") as file:
            self.HIGH_SCORE = int(file.read())
