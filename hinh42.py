import turtle

window = turtle.Screen()
window.title("Hinh43")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(15)

def w():
    pen.circle(30)
    pen.lt(50)
    pen.lt(14)
for _ in range(6):
    w()
    pen.lt(360/6)
turtle.done()