color1 = 'red'
color2 = 'blue'
color3 = 'purple'
color4 = 'orange'
color5 = 'cyan'
color6 = 'teal'

from turtle import*

for color in ["red", "blue", "purple", "orange", "cyan", "black",]:
    shape("circle")

    penup()
    fillcolor(color)
    stamp()
    forward(50)

hideturtle()



mainloop()


