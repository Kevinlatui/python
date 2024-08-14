import turtle

window = turtle.Screen()
window.title("Hinh36")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)

def d():
    pen.circle(30)
    pen.penup()
    pen.fd(30)
    pen.pendown()
    pen.rt(360/6)
    
for _ in range(6):
    d()
pen.circle(30)
turtle.done()
