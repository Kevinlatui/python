import turtle

window = turtle.Screen()
window.title("Hinh42")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(15)

def w():
    pen.circle(30)
    pen.rt(1)
for _ in range(6):
    w()
    pen.lt(360/6)
pen.penup()
pen.lt(90)
pen.bk(30)
pen.rt(90)
pen.pendown()
pen.circle(30)
turtle.done()