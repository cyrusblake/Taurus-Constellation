import turtle
import time

my_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
turtle.bgcolor("grey")
turtle.title("The Taurus Constellation")


def screen1():
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.write("Midterm Project", align="center", font=('', 50))
    turtle.right(90)
    turtle.penup()
    turtle.fd(50)
    turtle.sety(-10)
    turtle.pendown()
    turtle.write("The Taurus Constellation", align="center", font=('', 50))
    turtle.penup()
    turtle.fd(50)
    turtle.sety(-100)
    turtle.pendown()
    turtle.write("Cyrus Blake", align="center", font=('', 50))


screen1()
time.sleep(5)
turtle.clear()


def screen2():
    turtle.bgpic('R.png')
    turtle.color('blue')
    turtle.right(90)
    turtle.penup()
    turtle.fd(50)
    turtle.sety(-10)
    turtle.write("Taurus Constellation", align="center", font=('', 50))


screen2()
time.sleep(5)
turtle.clear()


def screen3():
    turtle.bgpic('')
    turtle.bgcolor("white")
    turtle.penup()
    turtle.pencolor('blue')

    turtle.goto(100, 100)
    turtle.write("Auriga")
    turtle.pendown()
    turtle.dot(10)

    turtle.penup()
    turtle.goto(250, -50)
    turtle.dot(10)

    turtle.penup()
    turtle.goto(300, -150)
    turtle.dot(10)

    turtle.penup()
    turtle.goto(350, -200)
    turtle.dot(10)

    turtle.penup()
    turtle.goto(350, -250)
    turtle.dot(10)

    turtle.penup()
    turtle.goto(300, -250)
    turtle.dot(10)

    turtle.penup()
    turtle.goto(250, -200)
    turtle.write("Aldebaran")
    turtle.dot(10)

    turtle.penup()
    turtle.goto(50, 50)
    turtle.dot(10)

    turtle.penup()
    turtle.goto(400, -350)
    turtle.dot(10)

    turtle.penup()
    turtle.goto(550, -500)
    turtle.dot(10)


screen3()
time.sleep(10)
turtle.clear()


def screen4():
    turtle.bgpic('stars.png')
    turtle.penup()
    turtle.pencolor('blue')

    turtle.goto(100, 100)
    turtle.write("Auriga")
    turtle.pendown()
    turtle.dot(10)

    turtle.penup()
    turtle.goto(250, -50)
    turtle.dot(10)

    turtle.penup()
    turtle.goto(300, -150)
    turtle.dot(10)

    turtle.penup()
    turtle.goto(350, -200)
    turtle.dot(10)

    turtle.penup()
    turtle.goto(350, -250)
    turtle.dot(10)

    turtle.penup()
    turtle.goto(300, -250)
    turtle.dot(10)

    turtle.penup()
    turtle.goto(250, -200)
    turtle.write("Aldebaran")
    turtle.dot(10)

    turtle.penup()
    turtle.goto(50, 50)
    turtle.dot(10)

    turtle.penup()
    turtle.goto(400, -350)
    turtle.dot(10)

    turtle.penup()
    turtle.goto(550, -500)
    turtle.dot(10)

    """





    """

    turtle.penup()

    turtle.goto(100, 100)

    turtle.pendown()

    turtle.goto(250, -50)

    turtle.goto(300, -150)

    turtle.goto(350, -200)

    turtle.goto(350, -250)

    turtle.goto(300, -250)

    turtle.goto(250, -200)

    turtle.goto(50, 50)

    turtle.penup()
    turtle.goto(350, -250)
    turtle.pendown()
    turtle.goto(400, -350)
    turtle.pendown()
    turtle.goto(550, -500)

    turtle.penup()


screen4()
time.sleep(10)
turtle.clear()
turtle.done()