import turtle as t
t.speed(0)
t.penup()
t.goto(-150,-150)
t.pendown()
for i in range(30):
    t.lt(12)
    t.circle(10,60)
    t.circle(-10,60)
    t.circle(10,60)
    t.circle(-10,60)
    t.circle(10,60)
    t.circle(-10,60)
