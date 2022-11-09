import turtle as a
import random as r
def star():
    a.colormode(255)
    a.fillcolor(r.randint(0,255),r.randint(0,255),r.randint(0,255))
    a.begin_fill()
    for i in range(5):
        a.hideturtle()
        a.forward(50)
        a.left(180-36)
    a.end_fill()
a.speed(20)
a.setup(900,662)
a.bgpic("D:\stars.png")
for q in range(r.randint(50,100)):
    a.penup()
    a.goto(r.randint(-450,450),r.randint(-331,331))
    a.pendown()
    star()
    
