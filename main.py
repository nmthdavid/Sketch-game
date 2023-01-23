from turtle import Turtle, Screen

def move_forward():
    t.forward(10)

def move_backward():
    t.forward(10)

def turn_right():
    t.right(10)

def turn_left():
    t.left(10)

def clearboard():
    screen.reset()


t = Turtle()
screen = Screen()
screen.title("Sketch game")
screen.listen()
screen.onkey(move_forward,"Up")
screen.onkey(move_backward,"Down")
screen.onkey(turn_right,"Right")
screen.onkey(turn_left,"Left")
screen.onkey(clearboard,"c")

screen.exitonclick()
