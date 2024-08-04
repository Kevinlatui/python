import turtle
window = turtle.Screen()
window.title("hinh21")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(3)

def f():
    pen.lt(90)
    pen.fd(150)
    pen.lt(90)
    pen.fd(50)
    pen.lt(90)
    pen.fd(50)
    pen.lt(90)
    pen.fd(50)
    pen.lt(90)
f()
turtle.done()