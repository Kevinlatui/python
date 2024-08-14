import turtle

window = turtle.Screen()
window.title("Hinh36")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(10000)

def d():
    pen.circle(30)
    pen.penup()
    pen.fd(30)
    pen.pendown()
    pen.rt(360/6)
    
for _ in range(6):
    d()
pen.penup()
pen.rt(90)
pen.fd(55)
pen.lt(90)
pen.fd(15)
pen.pendown()
pen.circle(30)
turtle.done()
