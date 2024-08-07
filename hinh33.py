import turtle

window = turtle.Screen()
window.title("Hinh33")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)

def g(circle):
    circle = 30    
    for _ in range(4):
        pen.fd(10)
        pen.lt(180)
        pen.fd(10)
        pen.rt(90) 
    for _ in range(2):
        pen.penup()
        pen.fd(30)
        pen.lt(90)
        pen.pendown()
        pen.circle(circle)
        circle = circle * 1.5  
        pen.penup()
        pen.fd(30)
        pen.pendown()
        pen.lt(90)       
        pen.circle(circle)




g(30)

turtle.done()