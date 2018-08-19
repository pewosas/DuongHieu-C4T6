from turtle import *
from random import randint
width (4)
colormode (255)
n = 1
for i in range (1, 400, 10):
    forward (n)
    left (90)
    forward (n)
    left (90)
    n = n+10
    o = randint(0, 255)
    m = randint(0, 255)
    l = randint(0, 255)
    color(n, m, l)

mainloop()