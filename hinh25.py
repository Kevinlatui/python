import turtle

window = turtle.Screen()
window.title("Hinh25")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(5)

def g():
    pen.lt(90)
    pen.fd(80)
    pen.lt(45)
    pen.fd(25)
    pen.rt(180)
    pen.fd(25)
    pen.lt(100)
    pen.fd(25)
    pen.lt(180)
    pen.fd(25)
    pen.lt(35)
    pen.fd(80)
pen.lt(90)
for _ in range(6):
    g()
    pen.lt(360/6)

turtle.done()