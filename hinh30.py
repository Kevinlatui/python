import turtle

window = turtle.Screen()
window.title("Hinh29")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(5)

def canh():
    pen.fd(100)
    pen.rt(60)
    pen.fd(100)
    pen.rt(150)
    pen.fd(173)
    pen.rt(150)
pen.lt(90)
for _ in range(9):
    canh()
    pen.lt(360/9)
turtle.done()

