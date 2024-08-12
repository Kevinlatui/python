import turtle

window = turtle.Screen()
window.title("Hinh43")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(15)

def w():
    pen.lt(90)
    pen.circle(30)
    pen.rt(50)
    pen.rt(14)
for _ in range(20):
    w()
    pen.rt(360/20)
turtle.done()
