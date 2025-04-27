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



import turtle

# window = turtle.Screen()
# window.setup(width=600,height=400)
# t = turtle.Turtle()
# t.down()
# t.shape("triangle")
# t.fillcolor("white")
# window.mainloop()

window = turtle.Screen()
window.setup(width=600,height=400)
t = turtle.Turtle()
t.penup()
t.goto(0,200)
t.down()
t.sety(-200)
t.penup()
t.goto(-300,0)
t.seth(290)
t.forward(600)
window.mainloop()

