import turtle

window = turtle.Screen()
window.title("ghen")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("circle")
pen.speed(0)
pen.color("red")

def f():
    for _ in range(3):
        pen.fd(60)
        pen.rt(120)
for _ in range(6):
    f()
    pen.fd(30)
    pen.lt(360/6)
turtle.done()
    