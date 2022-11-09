import turtle
while True:
    a = int(input("请输入一个边数(至少3条边，不能太大！)"))
    b = 360 / a
    for i in range(a):
        turtle.forward(100)
        turtle.left(b)
        turtle.hideturtle()
    c = input("是否继续？（yes/no）")
    if c == "no":
        break
        
        
