import turtle

window = turtle.Screen()
window.title("Hinh36")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(16666665)
pen.pensize(5)

def a():
    pen.color("blue")
    pen.circle(40)
    pen.rt(360/4)
    pen.color('yellow')
    pen.circle(40)
    pen.penup()
    pen.rt(230)
    pen.fd(60)
    pen.rt(50)
    pen.fd(10)
    pen.rt(90)
    pen.pendown()
    pen.color('black')
    pen.circle(40)
    pen.penup()
    pen.fd(40)
    pen.lt(90)
    pen.fd(50)
    pen.rt(90)
    pen.fd(-15)
    pen.pendown()
    pen.color("green")
    pen.circle(40)
    pen.penup()
    pen.lt(90)
    pen.fd(40)
    pen.lt(90)
    pen.fd(10)
    pen.rt(90)
    pen.fd(40)
    pen.pendown()
    pen.color('red')
    pen.circle(40)
a()
turtle.done()
