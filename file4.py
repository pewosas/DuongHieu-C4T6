from turtle import *
colormode(255)
n = 150
from random import randint
for i in range (1, 6):
    e = randint(100, 255)
    m = randint(200, 255)
    l = randint(120, 255)
    color(n, m, l)
    begin_fill()
    forward (n)
    left (90)
    forward (n)
    left (90)
    forward (n)
    left (90)
    forward (n)
    left (90)
    n = n-30
    end_fill()
mainloop()