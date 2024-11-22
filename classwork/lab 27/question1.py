'''
Write a few lines of code to observe the arrow direction using the positive and negative argument
in forward() function. Create this on orange background with the title, Figure(123).
'''

import turtle
t1 = turtle.Turtle()
t1.screen.title('First Turtle file')
t1.screen.bgcolor("orange")
t1.color('white')
t1.pensize(5)
t1.fillcolor('yellow')
t1.forward(-80)
t1.left(90)
t1.forward(50)
t1.left(-90)
t1.forward(80)

turtle.done()
