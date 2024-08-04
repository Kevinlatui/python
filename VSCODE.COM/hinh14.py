import turtle

window = turtle.Screen()
window.title("HInh14")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(10)
pen.color("blue")

def f():
    for _ in range(4):
        pen.fd(50)
        pen.rt(90)
for _ in range(10):
    f()
    pen.fd(30)
    pen.lt(360/10)
turtle.done()