import turtle

window = turtle.Screen()
window.title("Hinh43")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(1)

for _ in range(20):
    pen.circle(30)
    # pen.lt(50)
    # pen.lt(14)
    pen.lt(360/20)
turtle.done()

