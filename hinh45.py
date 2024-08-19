import turtle

window = turtle.Screen()
window.title("Hinh43")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(25)

for _ in range(45):
    pen.circle(30)
    pen.fd(10)
    pen.rt(360/45)
turtle.done()