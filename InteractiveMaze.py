'''
Create a Simple Maze and navigate it
'''

import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")

a = turtle.Turtle()

a = turtle.Turtle()
a.speed(1)
a.pensize(8)

# intro message
a.penup()
a.goto(-50,-100)
a.color("black")
a.pendown()
a.write("Welcome to the Interactive Maze Game!", font=(24))

# creating the maze walls
a.color("green")
a.penup()
a.goto(0,0)
a.pendown()
a.left(90)
a.forward(100)

a.penup()
a.goto(20,0)
a.pendown()
a.forward(80)
a.right(90)
a.forward(50)
a.right(90)
a.forward(70)
a.left(90)
a.forward(50)
a.left(90)
a.forward(20)
a.left(90)
a.forward(30)
a.right(90)
a.forward(150)
a.right(90)
a.forward(40)
a.right(90)
a.forward(30)
a.penup()

a.left(90)
a.forward(20)
a.pendown()
a.left(90)
a.forward(50)
a.left(90)
a.forward(80)
a.left(90)
a.forward(100)
a.right(90)
a.forward(70)
a.penup()

# user runs the maze
a.goto(10,0)
a.right(90)
a.color("purple")
a.pensize(4)
a.speed(4)
a.pendown()

# 90 is the correct answer
distance1 = 0.0
distance1 = int(screen.textinput("Input", "Enter distance to travel:"))
a.forward(distance1)
a.right(90)

# 70 correct
distance2 = 0.0
distance2 = int(screen.textinput("Input", "Enter distance to travel:"))
a.forward(distance2)
a.left(90)

# 100 then 60 then 50
for i in range(3):
    distance3 = 0.0
    distance3 = int(screen.textinput("Input", "Enter distance to travel:"))
    a.forward(distance3)
    a.right(90)

# display message
a.penup()
a.goto(10,-20)
a.color("black")
a.pendown()
a.write("If you didn't reach the end, try , try again!", font=(20))

# end program
turtle.done()

