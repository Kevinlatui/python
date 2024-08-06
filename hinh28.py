import turtle

window = turtle.Screen()
window.title("hinh28")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)

def s():
    pen.lt(90)
    pen.fd(80)
    pen.lt(150)
    for _ in range(12):
        pen.fd(10)
        pen.lt(180)
        pen.fd(10)
        pen.lt(360/12)
    pen.lt(30)
    pen.fd(80)
    pen.lt(90)
for _ in range(12):
    s()
    pen.lt(360/12)
turtle.done()