import turtle

window = turtle.Screen()
window.title("Hinh17")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("triangle")
pen.speed(4)

def fgh(canh):
    for _ in range(4):
        pen.fd(canh)
        pen.rt(90)

canh = 150

pen.lt(45)
for _ in range(3):
    fgh(canh)
    pen.penup()
    pen.rt(45)
    pen.fd(35)
    pen.lt(45)
    pen.pendown()
    canh = canh-50

turtle.done()