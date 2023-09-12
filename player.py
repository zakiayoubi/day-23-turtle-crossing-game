from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto_starting_line()
        self.left(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def goto_starting_line(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
