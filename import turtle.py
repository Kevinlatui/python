import turtle

window = turtle.Screen()
window.title("Hinh43")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)

def w():
    pen.rt(90)
    pen.circle(30)
    pen.lt(50)
    pen.lt(14)
for _ in range(20):
    w()
    pen.lt(360/20)
turtle.done()

