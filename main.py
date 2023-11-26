import turtle
from turtle import Screen
import time
import snake
import food
import scoreboard

# set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
score = scoreboard.Scoreboard()

# detect snake turns
turtle.listen()
turtle.onkeypress(snake.turn_left, "Left")
turtle.onkeypress(snake.turn_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()
    screen.update()

    # detect eating food
    if snake.head.distance(food) < 10:
        food.move()
        score.increase_score()
        snake.extend()

    snake.turn_permission(True)

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.update_highscore()
        score.game_over()
        snake.clear()
        food.clear()
        screen.update()

    # detect collision with snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.update_highscore()
            score.game_over()
            snake.clear()
            food.clear()
            screen.update()

screen.exitonclick()

