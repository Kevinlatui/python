import turtle

window = turtle.Screen()
window.title("Hinh36")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)

def d():
    pen.circle(30)
    pen.rt(120)
    
for _ in range(6):
    d()
turtle.done()
