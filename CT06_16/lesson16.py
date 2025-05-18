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
def CheckX(ball,screenWidth):
    if ball.xcor() > (screenwidth/2) or ball.xcor() < (-screenWidth/2)

screenWidth = 300
screenHeight = 500
window = setup(screenWidth,screenHeight)
ball = BlueBall()
dx = 2
dy = 2
while True:
    MoveBall(ball,dx,dy)
window.mainloop()