class Snake:
    from turtle import Turtle

    STARTING_POSITION = [(0, 0), (-20, - 0), (-40, 0)]
    TURN_PERMISSION_FLAG = True
    MOVE_DISTANCE = 20

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = self.Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        position = self.segments[-1].position()
        self.add_segment(position)

    def move(self, ):
        for n in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[n - 1].xcor()
            new_y = self.segments[n - 1].ycor()
            self.segments[n].goto(x=new_x, y=new_y)
        self.head.forward(self.MOVE_DISTANCE)

    def turn_right(self):
        if self.TURN_PERMISSION_FLAG:
            self.head.right(90)
            self.TURN_PERMISSION_FLAG = False

    def turn_left(self):
        if self.TURN_PERMISSION_FLAG:
            self.head.left(90)
            self.TURN_PERMISSION_FLAG = False

    def turn_permission(self, flag):
        self.TURN_PERMISSION_FLAG = flag

    def clear(self):
        for segment in self.segments:
            segment.hideturtle()

