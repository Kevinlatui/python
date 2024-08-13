import turtle

window = turtle.Screen()
window.title("Hinh35")
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("classic")
pen.speed(-1)

def ve_hinh_tron(ban_kinh):
    pen.penup()
    pen.goto(0, -ban_kinh)
    pen.pendown()
    pen.circle(ban_kinh)
    
for i in range(100, 69, -30):
    ve_hinh_tron(i)
    
for _ in range(12):
    pen.penup()
    pen.goto(0, 0)
    pen.rt(360/12)
    pen.fd(100)
    pen.pendown()
    pen.bk(30)


turtle.done()