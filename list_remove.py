color_list = ["red", "blue", "yellow", "teal"]
print("* " * 10)
command = input("What's your commnad (add, remove, draw)?")
while True:
    if command == "remove":

        print("old color:")
        color_to_remove = input("color_to_remove?")
        color_list.remove(color_to_remove)


    elif command == "add":

        color_to_append = input("color_to_append?")
        color_list.append(color_to_append)


    elif command == "draw":

        from turtle import*
        shape("turtle")
        hideturtle()
        penup()
        for c in color_list:
            fillcolor(c)
            stamp()
            forward(20)
            left(30)
        mainloop()


    for c in color_list:
        print(c)
    print("* " * 10)