import turtle
def setup(screenWidth,screenHeight):
    window = turtle.Screen()
    window.setup(width = screenWidth,height = screenHeight)
    return window
def BlueBall():
    t = turtle.Turtle
screenWidth = 300
screenHeight = 500
window = setup(screenWidth,screenHeight)
window.mainloop()