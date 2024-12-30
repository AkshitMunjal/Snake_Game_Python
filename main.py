from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score


sc = Screen()
sc.setup(600,600)
sc.title("My Snake Game ")
sc.bgcolor("black")
sc.tracer(0)

snake = Snake()
# snake.make_snake()
food = Food()
score = Score()

sc.listen()
sc.onkey(snake.up_key,"Up")
sc.onkey(snake.down_key,"Down")
sc.onkey(snake.left_key,"Left")
sc.onkey(snake.right_key,"Right")


is_game = True

while is_game:
    sc.update()
    time.sleep(0.1)

    snake.move_snake()

    if snake.head.distance(food.dot) < 15:
        food.rand_location()
        score.current_score = score.current_score + 1
        score.update_score()
        sc.update()
        snake.grow_snake()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset_snake()


    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 10:
            score.reset()
            snake.reset_snake()

sc.exitonclick()
