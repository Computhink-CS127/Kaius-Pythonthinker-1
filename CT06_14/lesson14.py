# import turtle
# window = turtle.Screen()
# window.setup(width=600,height=400)
# # t = turtle.Turtle()
# # t.shape("turtle")
# # t.fillcolor("orange")

# ## Task 3: Drawing
# # Given the number of sides and each interior angle, draw each of the
# # following shapes using a loop and the following functions:
# #     .seth()
# #     .up()
# #     .down()
# #     .forward()
# #     .backward()
# #     .left()
# #     .right()

# # **Task 3a**: Draw a line
# # Number of sides: 1
# # Interior angle: NA

# # **Task 3b**: Draw a triangle
# # Number of sides: 3
# # Interior angle: 120

# # **Task 3c**: Draw a square
# # Number of sides: 4
# # Interior angle: 90

# # **Task 3d**: Draw a pentagon
# # Number of sides: 5
# # Interior angle: 72

# # **Task 3e**: Draw a hexagon
# # Number of sides: 6
# # Interior angle: 60

# # **Task 3f**: Draw a circle
# # Number of sides: 360
# # Interior angle: 1


# t = turtle.Turtle()
# for i in range(4):
#     t.forward(100)
#     t.left(360/4)

# window.mainloop()



# import turtle
# import random
# window = turtle.Screen()
# window.setup(width=600,height=400)
# t = turtle.Turtle()
# t.down()
# t.shape("triangle")
# t.fillcolor("white")
# window.mainloop()

# window = turtle.Screen()
# window.setup(width=600,height=600)
# t = turtle.Turtle()
# t.penup()
# t.goto(0,200)
# t.down()
# t.sety(-200)
# t.penup()
# t.goto(-300,0)
# t.down()
# t.setx(300)
# window.mainloop()

# import turtle
# import random

# screen = turtle.Screen()
# screen.setup(600, 600)

# t = turtle.Turtle()


# for i in range(10):
#     x, y = random.randint(-280, 280), random.randint(-280, 280)
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     for i in range(4):
#         t.forward(5)
#         t.left(90)
#     t.penup()
#     t.goto(x, y - 40)
#     t.write(t.pos(),align="center")

# t.hideturtle()
# turtle.done()

import turtle
screen = turtle.Screen()
screen.setup(400, 400)
t = turtle.Turtle()
t.penup()
t.goto(-200, -200)
t.pendown()

while True:
    while t.xcor() < 200:
        t.forward(1)
    t.left(90)

    while t.ycor() < 200:
        t.forward(1)
    t.left(90)

    while t.xcor() > -200:
        t.forward(1)
    t.left(90)

    while t.ycor() > -200:
        t.forward(1)
    t.left(90)

# Task 6
# import turtle

# window = turtle.Screen()

# window.setup(width=400, height=400)

# t = turtle.Turtle()
# t.shape("turtle")
# t.fillcolor("green")

# x_limit = 180
# y_limit = 180

# t.penup()

# t.goto(-x_limit, -y_limit) # Go to bottom left

# t.pendown()
# while True:
#     while t.xcor() < x_limit: # draw horizontal line towards the right
#         t.forward(1)
#     t.left(90)
#     while t.ycor() < y_limit: # draw vertical line upwards
#         t.forward(1)
#     t.left(90)
#     while t.xcor() > -x_limit: # draw horizontal line towards the left
#         t.forward(1)
#     t.left(90)
#     while t.ycor() > -y_limit: # draw vertical line downwards
#         t.forward(1)
#     t.left(90)

#     break
    
# window.mainloop()