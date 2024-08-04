import turtle

window = turtle.Screen()
window.title("Hinh19")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)

pen.rt(45)
def h():
  for _ in range(4):
    pen.fd(40)
    pen.rt(90)

for _ in range(5):
  h()
  pen.penup()
  pen.lt(45)
  pen.fd(10)
  pen.rt(45)
  pen.pendown()

turtle.done()