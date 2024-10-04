import turtle

window = turtle.Screen()
window.title("Hinh43")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)

def tranh():
    for _ in range(4):
        pen.fd(100)
        pen.rt(90)
    pen.penup()
    pen.fd(50)
    pen.rt(90)
    pen.fd(50)
    pen.pendown()
    for _ in range(4):
        for _ in range(1):        
            pen.circle(50 ,90)
            pen.lt(90)
            pen.circle(50 ,90)
            pen.lt(90)
            pen.rt(270)

tranh()
turtle.done()