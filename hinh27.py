import turtle

window = turtle.Screen()
window.title("Hinh27")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(5)

def f():
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
    f()
    pen.rt(90)
turtle.done()