import turtle

window = turtle.Screen()
window.title("Hinh36")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(15)

def a():
    pen.lt(90)
    pen.fd(100)
    pen.circle(20)
    pen.rt(180)
    pen.fd(100)
    pen.lt(90)
for _ in range(10):
    a()
    pen.rt(36)
turtle.done()