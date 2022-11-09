import turtle as a
import random as b
a.speed(10)
a.pensize(2)
a.setup(500,500)
q = 0
a.colormode(255)
while q<36:
    a.pencolor(b.randint(0,255),b.randint(0,255),b.randint(0,255))
    a.left(10)
    for d in range(5):
        a.left(72)
        a.forward(50)
    q=q+1
    d=d+1
q = 0
while q<36:
    a.pencolor(b.randint(0,255),b.randint(0,255),b.randint(0,255))
    a.circle(100)
    a.left(10)
    q=q+1
    
