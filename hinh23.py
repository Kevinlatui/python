import turtle

window = turtle.Screen()
window.title("H")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(10)

def h():
    pen.lt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(25)
    pen.rt(90)
    pen.fd(50)
    pen.rt(90)
    pen.fd(50)
    pen.rt(90)
    pen.fd(50)
    pen.rt(90)
    pen.fd(25)
    pen.penup()
    pen.lt(90)
    pen.fd(100)
    pen.pendown()
for _ in range (6):
    h()
    pen.lt(360/12)

turtle.done()
