from turtle import *

shape ("turtle")
colormode(255)
width(5)
for i in range(40):
    color(255 - i * 5, i * 5, i * 5)
    forward(i * 5)
    left(90)

mainloop()