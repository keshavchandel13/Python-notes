import turtle
import math
t1 = turtle.Turtle()
t1.screen.title('Curve')
t = 0.1
c = 2
PI = math.pi
scale = 50
while t < PI:
    val = c * t
    x = scale * math.sin(val)
    y = scale * math.cos(val)
    t1.goto(x, y)
    t += 0.1

turtle.done()
