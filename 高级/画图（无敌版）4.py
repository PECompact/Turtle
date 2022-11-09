import turtle as t
t.penup()
t.goto(0,0)
t.pendown()
t.speed(0)
t.color("red")
def t_1(n):
    t.setup(600,600)
    if n<=5:
        return 1
    else:
        for i in range(5):
            t.forward(n)
            t.left(144)
            t_1(n/3)
number = (100)
t_1(number)
