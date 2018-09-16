color_list = ["red", "purple", "blue", "orange", "teal"]
while True:
    new_color = input("New_color?")
    color_list.append(new_color)
    print("* " * 10)

    for color in color_list:
        print(color)
    print("* " * 10)