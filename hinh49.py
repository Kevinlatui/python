import turtle

window = turtle.Screen()
window.title("Hinh43")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)

for _ in range(4):
    pen.fd(100)
    pen.rt(90)
pen.fd(100)
pen.lt(180)
pen.circle(100 , 90)
pen.rt(270)
pen.fd(100)
pen.lt(90)
pen.circle(50 , 180)
pen.rt(90)
pen.bk(100)
pen.lt(90)
pen.bk(100)
pen.rt(90)
pen.circle(50 , 180)
turtle.done()