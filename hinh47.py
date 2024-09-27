import turtle
from random import randint
def mau():
    pen.pencolor(randint(0,255),randint(0 , 255),randint(0,255))


window = turtle.Screen()
window.title("Hinh43")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)


window.colormode(255)

for _ in range(180 ):
    pen.fd(90)
    pen.bk(90)
    pen.lt(1)
    mau()
    
turtle.done()