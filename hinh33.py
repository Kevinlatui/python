import turtle

window = turtle.Screen()
window.title("Hinh33")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)


# circle = 30    
for _ in range(4):
    pen.fd(10)
    pen.lt(180)
    pen.fd(10)
    pen.rt(90) 
    
def f(g):
    g = 30
    pen.penup()
    pen.fd(30)
    pen.lt(90)
    pen.pendown()
    pen.circle(g) 
    pen.penup()
    pen.rt(90)
    pen.fd(10)
    pen.left(90)
    pen.pendown()
# pen.lt(50)       
    pen.circle(g+10)
    pen.penup()
    pen.right(90)
    pen.forward(10)
    pen.left(90)
    pen.pendown()
    pen.circle(g+20)
    pen.penup()
    pen.right(90)
    pen.forward(10)
    pen.left(90)
    pen.pendown()
    pen.circle(g+30)
    
f(30)
turtle.done()