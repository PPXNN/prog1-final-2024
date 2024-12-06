import turtle
import random


class Ball:
    def __init__(self, color,  size, x, y, vx, vy):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def draw_ball(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_ball(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def update_ball_velocity(self, canvas_width, canvas_height):
        if abs(self.x) > (canvas_width - self.size):
            self.vx = -self.vx

        if abs(self.y) > (canvas_height - self.size):
            self.vy = -self.vy

class Simulation:
    def __init__(self, num):
        self.num_ball = num
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        self.balls = []
        self.dt = 0.2
        self.create()

        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

    def create(self):
        for i in range(self.num_ball):
            x = random.uniform(-1*self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius)
            y = random.uniform(-1*self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius)
            vx = 10*random.uniform(-1.0, 1.0)
            vy = 10*random.uniform(-1.0, 1.0)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.balls.append(Ball(color, self.ball_radius, x, y, vx, vy))

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)

    def update(self):
        turtle.clear()
        self.draw_border()
        for i in self.balls:
            i.draw_ball()
            i.move_ball(self.dt)
            i.update_ball_velocity(self.canvas_width, self.canvas_height)
        turtle.update()

    def run(self):
        while True:
            self.update()
            for j in range(1, 10):
                self.update()
                turtle.update()
                self.update()
                count.clear()
                self.update()
                count.draw(j)
                self.update()
                count.my_delay(delay_in_seconds)
                self.update()

class Count:
    def __init__(self, my_turtle, color):
        self.my_turtle = my_turtle
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

        self.my_turtle.color(color)
        self.my_turtle.penup()
        self.my_turtle.setheading(0)
        self.my_turtle.goto(0, 0)
        self.my_turtle.pensize(10)

    def draw(self,digit):
        if digit == 0:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.penup()

        if digit == 1:
            self.my_turtle.goto(50, 100)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 2:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.penup()

        if digit == 3:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 4:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.my_turtle.forward(-100)
            self.my_turtle.right(90)
            self.my_turtle.penup()

        if digit == 5:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 6:
            self.draw(5)
            self.my_turtle.goto(-50, 0)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 7:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.draw(1)

        if digit == 8:
            self.draw(0)
            self.my_turtle.goto(-50, 0)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.penup()

        if digit == 9:
            self.draw(5)
            self.my_turtle.goto(50, 100)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.penup()

    def clear(self):
        self.my_turtle.clear()

    def my_delay(self, dt):
        import time
        start = time.time()
        while time.time() - start < dt:
            pass


Tom = turtle.Turtle()
tom_color = (255, 0, 0)
count = Count(Tom, tom_color)
delay_in_seconds = 0.2
while True:
    ball = Simulation(5)
    ball.run()


    turtle.done()