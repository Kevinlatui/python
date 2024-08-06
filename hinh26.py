import turtle

window = turtle.Screen()
window.title("Hinh26")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(5)

def f():
    pen.lt(90)
    pen.fd(90)
    pen.lt(45)
    for _ in range(4):
        pen.fd(10)
        pen.rt(90)
    pen.lt(135)
    pen.fd(90)
    pen.lt(90)

for _ in range(6):   
    f()
    pen.lt(360/6)
turtle.done()
