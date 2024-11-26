'''Write a few lines of code to create a sheet with grid lines along x axis and y axis separated by 20
units of distance from one line to another line. Hide the turtle using Turtle state options.'''
import turtle

screen = turtle.Screen()
screen.bgcolor("white")


t1 = turtle.Turtle()
t1.speed(0)
t1.hideturtle()  

#  vertical lines
for x in range(-100, 200, 30):
    t1.penup()
    t1.goto(x, -200)
    t1.pendown()
    t1.goto(x, 200)
# horizontal lines
for y in range(-100, 200, 30):
    t1.penup()
    t1.goto(x, -200)
    t1.pendown()
    t1.goto(x, 200)




turtle.done()
