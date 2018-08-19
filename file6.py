from turtle import*
n = 20
from random import randint
colormode (255)
for i in range (1,11):
    e = randint(0, 255)
    m = randint(0, 255)
    l = randint(0, 255)
    color(n, m, l)
    begin_fill ()
    for i in range (1,5):
        forward (n)
        right (90)
    right (30)
    n = n + 20
    end_fill()
mainloop()