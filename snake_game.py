# import the libraries 
import turtle
import random

# set the width and hieght for the window 
w = 500
h = 500

# set the food size and delay time 
food_size = 10
delay = 100

# set the moves with position 
# how much snake move in each direction
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

# define function for the reset the position 
# use gloabl to declare variable as globaly so we can use it entire the program 
def reset():
    global snake, snake_dir, food_position, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]] # initial snake position
    snake_dir = "up"
    # get the random postion of food when start the game and set the position
    food_position = get_random_food_position()
    food.goto(food_position)
    move_snake()

# define function for the move of snake
def move_snake():
    global snake_dir
    # copy the new head postion of snake 
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]
 
    # if head of snake in the current position of sanke then restart the game  
    # else append the position
    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)

        # if not get the food then game continue
        if not food_collision():
            snake.pop(0)
 
        # check the snake position according to height and width
        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h
 
 
        pen.clearstamps()
 
        # move the snake according to segment
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()
 
        # update the screen 
        screen.update()
 
        turtle.ontimer(move_snake, delay)

# define function when snake and food hit 
def food_collision():
    global food_position
    # return true if the  snake last postion and food position distance less the 20
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False

# define function to ge the random position of food for defined window
def get_random_food_position():
    x = random.randint(- w / 2 + food_size, w / 2 - food_size)
    y = random.randint(- h / 2 + food_size, h / 2 - food_size)
    return (x, y)

# define function to get the distance between snake and food
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

# function to move up
def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"

# function to move right
def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"

# function to move down
def go_down():
    global snake_dir
    if snake_dir!= "up":
        snake_dir = "down"

# function to move left
def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"
 

# set the turtle screen and background color
screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake")
screen.bgcolor("blue")
screen.setup(500, 500) # screen size
screen.tracer(0)
 
# call the turtle with shape
pen = turtle.Turtle("square")
pen.penup() # move turtle without leaving tracks
 
# call the turtle function and also set shape and color
food = turtle.Turtle()
food.shape("square")
food.color("yellow")
food.shapesize(food_size / 20)
food.penup() # move turtle without leaving tracks
 
# set the movement as per on key press 
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
 
# call the reset function
reset()
turtle.done()