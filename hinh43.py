import turtle

window = turtle.Screen()
window.title("Hinh43")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(15)

pen.rt(90)
for _ in range(30):
    pen.circle(30)
    # pen.lt(50)
    # pen.lt(14)
    pen.lt(180/30)
turtle.done()

