from turtle import Turtle,Screen
from typing import List, Any

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:

    def __init__(self,shape):

        self.seg_list = []
        self.shape = shape
        self.create_snake()
        self.head=self.seg_list[0]
        self.tail=None




    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_segment(position)

    def move(self):

# Todo list - practice more on range printing
        for i in range(len(self.seg_list) - 1, 0, -1):  # Gotto practice more on range setting start and stop more

            new_x = self.seg_list[i - 1].xcor()
            new_y = self.seg_list[i - 1].ycor()

            self.seg_list[i].goto(new_x, new_y)

        self.head.forward(MOVING_DISTANCE)
    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:

            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def add_segment(self,position):
        segment = Turtle()
        segment.penup()
        segment.shape(self.shape)
        segment.color("white")
        segment.goto(position)
        self.seg_list.append(segment)


    def extendsnake(self):
        self.add_segment(self.seg_list[-1].position())









