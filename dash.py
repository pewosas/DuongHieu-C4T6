from turtle import *
colormode(255)
width(5)
hideturtle()


for i in range(10):
    if i % 5 == 0:
        color("blue")
    else:
        color("red")
    forward(20)
    penup()
    forward(20)
    pendown()



mainloop()