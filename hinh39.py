import turtle

window = turtle.Screen()
window.title("Hinh36")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)

def a():
    pen.lt(90)
    pen.fd(100)
    pen.circle(20)
a()
turtle.done()