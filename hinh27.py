import turtle

window = turtle.Screen()
window.title("Hinh27")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(2)

def d():
    pen.lt(90)
    pen.fd(90)
    pen.lt(90)
    pen.fd(90)
    pen.lt(90)
    pen.fd(45)
    pen.lt(90)
    pen.fd(45)
    pen.rt(180)
    pen.fd(45)
    pen.rt(90)
    pen.fd(45)
    pen.rt(90)
    pen.fd(90)
    pen.rt(90)
    pen.fd(90)
    pen.lt(90)
for _ in range(4):   
    d()
    pen.rt(90)
turtle.done()