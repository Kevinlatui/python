import turtle

window = turtle.Screen()
window.title("Hinh31")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(5)

pen.lt(60)
def f():
    pen.fd(50)
    pen.lt(45)
    pen.fd(100)
    pen.lt(150)
    pen.fd(100)
    pen.lt(45)
    pen.fd(50)
    pen.rt(60)
for _ in range(8):  
    f()
    pen.rt(360/8)
turtle.done()