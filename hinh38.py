import turtle

window = turtle.Screen()
window.title("Hinh37")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)

def a():
    pen.lt(90)
    pen.fd(100)
    pen.rt(90)
    pen.circle(20)
    pen.lt(270)
    pen.fd(100)
    pen.lt(90)
    
for _ in range(10):
    a()
    pen.lt(360/10)
turtle.done()