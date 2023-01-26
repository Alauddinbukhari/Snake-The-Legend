from turtle import Turtle
ALIGNMENT ="center"
FONT =("Gooddog",25,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.color("White")
        self.penup()
        self.goto(x=0,y=270)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)



    def gameover(self):

        self.goto(0,0)


        self.write("Gameover",align=ALIGNMENT,font=FONT)





    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)



