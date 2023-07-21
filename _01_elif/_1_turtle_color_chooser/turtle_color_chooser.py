import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle

    x=turtle.Turtle()
    x.speed(1)
    while True:
        col=input("what color pen?")
        if col=="green":
            x.pencolor("green")
        elif col=="red":
            x.pencolor("red")
        elif col=="orange":
            x.pencolor("orange")
        elif col=="blue":
            x.pencolor("blue")
        else:
            x.pencolor(get_random_color())
        for i in range (4):
            x.forward(50)
            x.right(90)
        x.width(10)

    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
