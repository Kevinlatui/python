import turtle

window = turtle.Screen()
window.title("hinh15")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.color("blue")
pen.speed(0)

def g():
    for _ in range(5):
        pen.fd(50)
        pen.lt(360/5)
for _ in range(5):
    g()
    pen.fd(100)
    pen.lt(360/5)
turtle.done()