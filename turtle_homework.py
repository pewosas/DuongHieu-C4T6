from turtle import*
shape("turtle")


# from random import randint
#
# width(5)
# colormode(255)
# e = 110
# n = randint(0, 255)
# m = randint(0, 255)
# l = randint(0, 255)
# color(n, m, l)
# for i in range(1, 5):
#     forward(e)
#     left(90)
# n = randint(0, 255)
# m = randint(0, 255)
# l = randint(0, 255)
# color(n, m, l)
# for i in range(1, 6):
#     forward(e)
#     left(72)
# n = randint(0, 255)
# m = randint(0, 255)
# l = randint(0, 255)
# color(n, m, l)
# for i in range(1, 7):
#     forward(e)
#     left(60)
# n = randint(0, 255)
# m = randint(0, 255)
# l = randint(0, 255)
# color(n, m, l)
# for i in range(1, 8):
#     forward(e)
#     left(360 / 7)
#
# color(n, m, l)
# for i in range(1, 4):
#     forward(e)
#     left(120)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
n = 3
for i in colors:
    color(i)
    for a in range(n):
        forward(100)
        left(360/n)
    n += 1





mainloop()

