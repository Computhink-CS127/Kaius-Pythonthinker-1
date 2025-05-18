import turtle
def setup(screenWidth,screenHeight):
    window = turtle.Screen()
    window.setup(width = screenWidth,height = screenHeight)
    return window
def BlueBall():
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("blue")
    ball.penup()
    return ball
def MoveBall(ball,dx,dy):
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)


screenWidth = 300
screenHeight = 500
window = setup(screenWidth,screenHeight)
ball = BlueBall()
window.mainloop()