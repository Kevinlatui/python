import turtle

window = turtle.Screen()
window.title("Hinh22")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)

def h():
    pen.lt(90)
    pen.fd(150)
    pen.lt(90)
    pen.fd(50)
    pen.lt(90)
    pen.fd(50)
    pen.lt(90)
    pen.fd(50)
    pen.penup()
    pen.lt(270)
    pen.fd(100)
    pen.pendown()
for _ in range(8):
    h()
    pen.rt(360/8)
   
turtle.done()