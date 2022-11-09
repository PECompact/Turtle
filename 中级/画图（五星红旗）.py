import turtle as t
t.hideturtle()
t.speed(0)
#画长方形:
t.penup()
t.goto(-150,100)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.forward(450)
t.right(90)
t.forward(270)
t.right(90)
t.forward(450)
t.right(90)
t.forward(270)
t.right(90)
t.penup()
t.end_fill()


#画五角星:
t.goto(0,100)#上100像素
t.goto(-100,0)#左100像素
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
for i in range(5):    
    t.forward(100)
    t.right(144)
t.penup()
t.end_fill()


t.goto(25,80)
t.pendown()


t.fillcolor("yellow")
t.begin_fill()
for i in range(5):    
    t.forward(50)
    t.right(144)
t.penup()
t.end_fill()


t.goto(15,25)
t.pendown()


t.fillcolor("yellow")
t.begin_fill()
for i in range(5):    
    t.forward(50)
    t.right(144)
t.penup()
t.end_fill()


t.goto(5,-30)
t.pendown()


t.fillcolor("yellow")
t.begin_fill()
for i in range(5):    
    t.forward(50)
    t.right(144)
t.penup()
t.end_fill()


t.goto(-5,-85)
t.pendown()


t.fillcolor("yellow")
t.begin_fill()
for i in range(5):    
    t.forward(50)
    t.right(144)
t.penup()
t.end_fill()
