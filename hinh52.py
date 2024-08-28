import turtle

window = turtle.Screen()
window.title("Hinh43")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)
pen.pensize(10)

def w(diameter , minus_and_plus , fd):
    diameter = 100
    minus_and_plus = 10
    fd = 180
    pen.lt(90)
    pen.color('red')
    pen.circle(diameter , fd)
    pen.penup()
    pen.lt(90)
    pen.fd(fd + minus_and_plus)
    pen.lt(90)
    pen.pendown()
    pen.color('orange')
    pen.circle(diameter - minus_and_plus , fd)
    pen.penup()
    pen.lt(90)
    pen.fd(fd - minus_and_plus)
    pen.lt(90)
    pen.pendown()
    pen.color('yellow')
    pen.circle(diameter - (minus_and_plus * 2) , fd)
    pen.penup()
    pen.lt(90)
    pen.fd(fd - (minus_and_plus * 3))
    pen.lt(90)
    pen.pendown()
    pen.color('green')
    pen.circle(diameter - (minus_and_plus * 3) , fd)
    pen.penup()
    pen.lt(90)
    pen.fd(fd - (minus_and_plus * 5))
    pen.lt(90)
    pen.pendown()
    pen.color('cyan')
    pen.circle(diameter - (minus_and_plus * 4) , fd)
    pen.penup()
    pen.lt(90)
    pen.fd(fd - (minus_and_plus * 7))
    pen.lt(90)
    pen.pendown()
    pen.color('indigo')
    pen.circle(diameter - (minus_and_plus * 5) , fd)
    pen.penup()
    pen.lt(90)
    pen.fd(fd - (minus_and_plus * 9))
    pen.pendown()
    pen.lt(90)
    pen.color('violet')
    pen.circle(diameter - (minus_and_plus * 6) , fd)

        
    

w(60,10 , 180)
turtle.done()
    
    
    
    
    