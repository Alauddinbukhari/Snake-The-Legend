import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

score_board= Scoreboard()

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)


# create a snake
snake = Snake("square")
food= Food()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(snake.down,key="Down")
screen.onkey(snake.left,key="Left")
screen.onkey(snake.right,key="Right")

screen.listen()

# move the snake
gameison = True

while gameison:

    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
       food.refresh()
       snake.extendsnake()
       score_board.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        gameison=False
        # screen.clear()
        score_board.gameover()
    #Detect collision with tail
    for segament in snake.seg_list[1:]:

        if snake.head.distance(segament)<10:
            gameison=False
            score_board.gameover()







screen.exitonclick()
