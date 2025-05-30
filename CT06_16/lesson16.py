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
    if ball.xcor() > (screenWidth/2) or ball.xcor() < (-screenWidth/2):
        return True
def CheckY(ball,screenHeight):
    if ball.ycor() > (screenHeight/2) or ball.ycor() < (-screenHeight/2):
        return True


screenWidth = 300
screenHeight = 500
window = setup(screenWidth,screenHeight)
ball = BlueBall()
dx = 2
dy = 2
while True:
    MoveBall(ball,dx,dy)
    if CheckX(ball,screenWidth-20):
        dx *= -1
    elif CheckY(ball,screenHeight-20):
        dy *= -1
window.mainloop()