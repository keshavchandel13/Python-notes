''' Write a few lines of code to draw lines of thickness(width) 5, 10 and 15 with three dierent
lengths with tree colours red, green an blue.'''
import turtle

t1 = turtle.Turtle()
t1.screen.bgcolor('grey')
t1.pensize(5)
t1.color('red')
t1.forward(100)


t1.left(90)
t1.color('green')
t1.pensize(10)
t1.forward(100)

t1.left(90)
t1.color('blue')
t1.pensize(15)
t1.forward(100)

turtle.done()
