import turtle

window = turtle.Screen()
window.title("Hinh33")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)

def a():
    pen.circle(20)
    pen.rt(90)
    pen.fd(100)
a()
turtle.done()