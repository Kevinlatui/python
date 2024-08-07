import turtle

window = turtle.Screen()
window.title("Hinh33")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)

def g(circle):
    for _ in range(4):
        pen.fd(10)
        pen.lt(180)
        pen.fd(10)
        pen.rt(90)
    for _ in range(4):
        pen.penup()
        pen.fd(30)
        pen.lt(90)
        pen.pendown()
        pen.circle(circle)
        pen.penup()
        pen.fd(30)
        pen.pendown()
        pen.lt(90)
        pen.circle(circle*1.5)
circle = 30



g(circle)

turtle.done()