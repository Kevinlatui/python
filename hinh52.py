import turtle

window = turtle.Screen()
window.title("Hinh43")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)
pen.pensize(10)

def w(diameter , minus , fd):
    diameter = 100
    minus = 10
    fd = 180
    pen.color('red')
    pen.circle(diameter , fd)
    pen.penup()
    pen.lt(90)
    pen.fd(10)
    pen.pendown()




    pen.penup()



    pen.circle(diameter - minus , fd)
    pen.pendown()
    pen.color('orange')
    pen.rt(90)
    pen.circle(diameter - minus , fd)
    pen.penup()
    pen.lt(90)
    pen.fd(10)
    pen.pendown()
    pen.color('yellow')
    pen.rt(90)
    pen.circle(diameter - (minus * 2) , fd)
    pen.penup()
    pen.lt(90)
    pen.fd(10)
    pen.pendown()
    pen.color('green')
    pen.rt(90)
    pen.circle(diameter - (minus * 3) , fd)
    pen.penup()
    pen.lt(90)
    pen.fd(10)
    pen.pendown()
    pen.color('cyan')
    pen.rt(90)
    pen.circle(diameter - (minus * 4) , fd)
    pen.penup()
    pen.lt(90)
    pen.fd(10)
    pen.pendown()
    pen.color('indigo')
    pen.rt(90)
    pen.circle(diameter - (minus * 5) , fd)
    pen.penup()
    pen.lt(90)
    pen.fd(10)
    pen.pendown()
    pen.color('violet')
    pen.rt(90)
    pen.circle(diameter - (minus * 6) , fd)
    pen.penup()
    pen.lt(90)
    pen.fd(10)
    
    
    

w(60,10 , 180)
turtle.done()
    