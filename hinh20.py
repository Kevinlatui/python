import turtle

window = turtle.Screen()
window.title("hinh20")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(2)

pen.rt(45)
def g(cd,cr):
    for _ in range(2):
        pen.fd(cd)
        pen.rt(90)
        pen.fd(cr)
        pen.rt(90)
cd = 20
cr = 20
g(cd,cr)
pen.penup()
pen.lt(180)
pen.fd(20)
pen.lt(90)
pen.pendown()
g(cd*3  , cr)
pen.penup()
pen.fd(cd*2)
pen.lt(90)
pen.fd(30)
pen.pendown()
g(cd*3 , cr)
pen.penup()
pen.fd(cd*3)
pen.lt(90)
pen.fd(30)
pen.pendown()
for _ in range(2):
    pen.fd(cd*3)
    pen.lt(90)
    pen.fd(cr)
    pen.lt(90)
pen.penup()
pen.fd(cd*3)
pen.lt(90)
pen.fd(50)
pen.pendown()
for _ in range(2):
    pen.fd(cd*3)
    pen.lt(90)
    pen.fd(cr)
    pen.lt(90)

turtle.done()   