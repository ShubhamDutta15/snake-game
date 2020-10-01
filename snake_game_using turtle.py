import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# set up the screen
win = turtle.Screen()                  # to create a window
win.title("Shubham's Snake game")        # to give a name to the window
win.bgcolor("green")                   # to give a background color for the window
win.setup(width=600, height=600)       # to set the window height and width
win.tracer(0)                          # turns off the screen update


# create the snake head
head = turtle.Turtle()                # create snake head
head.speed(0)                         # head animation speed is set to 0
head.shape("square")                  # head shape
head.color("black")                   # head color
head.penup()                          # path taken by snake is not drawn
head.goto(0, 0)                       # set the snake's head position to be at the center of the window
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# pen (here it is used to write score
# and high score in the top)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.shape("square")
pen.penup()
pen.hideturtle()               # to hide the turtle which is created
pen.goto(0,250)
pen.write(f"Score : 0       High Score:  {high_score}", align = "center", font = ("Arial", 25, "normal"))


# Snake cannot go right from left, left from right
# top from down, and down from top

def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"

segments = []
# Function


def move():
    if head.direction == "up":         # if head moves in upward direction
        y = head.ycor()                # y coordinate of the turtle
        head.sety(y + 20)                # y increases

    if head.direction == "down":       # if head moves in downward direction
        y = head.ycor()                 # x coordinate of the turtle
        head.sety(y - 20)                # y decreases

    if head.direction == "left":       # if head moves in left direction
        x = head.xcor()                # x coordinate of the turtle
        head.setx(x - 20)              # x decreases

    if head.direction == "right":      # if head moves in right direction
        x = head.xcor()                # x coordinates of the turtle
        head.setx(x + 20)              # x increases


# Keyboard bindings
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

# Main game loop
while True:
    win.update()                      # to update our window whatever in the code

    # Check for collison with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()             # clear all the pen written things
        pen.write(f"Score :  {score}     High Score: {high_score}", align="center", font=("Arial", 25, "normal"))

        # move the end segment in reverse order
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)          # move last segment to its second last segment
        # move segment 0 where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)       # 1st index is moved to the top of the head

    move()

    # add border collision
    if head.xcor() > 290 or head.xcor()< -290 or head.ycor() > 290 or head.ycor() <-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # segment's postion is set to outside the window
        for segment in segments:
            segment.goto(1000, 1000)

        # clear segments
        segments = []

        # reset score
        score = 0

        # update score
        pen.clear()               # clear all the pen written things
        pen.write(f"Score :  {score}     High Score: {high_score}", align="center", font=("Arial", 25, "normal"))

    # add body collision
    for segment in segments:
        # if distance between head
        # and segment is less thn or equal to 20
        if segment.distance(head) < 20:

            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # segment's postion is set to outside the window
            for segment in segments:
                segment.goto(1000, 1000)

            # clear segments
            segments = []

            # reset score
            score = 0
            # update score
            pen.clear()           # clear all the pen written things
            pen.write(f"Score :  {score}     High Score: {high_score}", align="center", font=("Arial", 25, "normal"))

    time.sleep(delay)


win.mainloop()


# dimension of each Turtle is by default to 20 X 20