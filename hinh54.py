import turtle

window = turtle.Screen()
window.title("Hinh43")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)

def cung():
    for _ in range(2):
        pen.circle(90 ,90)
        pen.lt(90)
for _ in range(8):
    cung()
    pen.rt(360/8)
turtle.done()