'''Wrire a progam to print the spiral whose equation is given as r = bθ.
+ Choose b as an integer. Increase θ from zero to a large number. Calculate r.
+ Then convert (r,θ) into rectangular coordinates and plot the spiral.'''
import turtle
import math


t1 = turtle.Turtle()
t1.screen.bgcolor('black')
t1.color('white')
t1.pensize(3)


b = 5
theta = 0


while theta < 60:
 for i in ['red','blue','green']:
    t1.color(i)
    r = b * theta
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    t1.goto(x, y)
    theta += 0.1 

turtle.done()
