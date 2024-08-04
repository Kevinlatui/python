import turtle

window = turtle.Screen()
window.title("henrietta")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(10)

def fgdfg(cd, cr):
    for _ in range(2):
        pen.fd(cd)
        pen.lt(90)
        pen.fd(cr)
        pen.lt(90)
        
cd = 40
cr = 40
for _ in range(4):      
    fgdfg(cr, cd)
    pen.penup()
    pen.fd(50)
    pen.pendown()
    cd = cd + cr
    


turtle.done()
    