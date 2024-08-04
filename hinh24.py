import turtle

window = turtle.Screen()
window.title("h")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(10)

def g():
    pen.lt(90)
    pen.fd(120)
    pen.lt(140)
    pen.fd(30)
    pen.lt(180)
    pen.fd(30)
    pen.rt(94)
    pen.fd(30)
    pen.lt(180)
    pen.fd(30)
    pen.rt(226)
    pen.fd(120)
for _ in range(6):
    g()
    pen.lt(360/12)
    
    
turtle.done()
