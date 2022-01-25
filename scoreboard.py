from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.pu()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"level: {self.level}", align='left', font=FONT)


    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAMEOVER", align='center' , font=FONT)