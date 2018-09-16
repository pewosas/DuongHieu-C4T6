#
# colors = ['red', 'blue', 'brown', 'yellow', 'grey']
# for i in colors:
#     print(i, end=", ")
# print()
#
# colors.append("black")
#
# for i in colors:
#     print(i, end=", ")
# print()
#
# colors[1] = "yellow"
#
# for i in colors:
#     print(i, end=", ")
# print()
#
# # del colors[1]
# colors.remove("red")
# for i in colors:
#     print(i, end=", ")
# print()



print("Welcome to our shop")
Our_items = ["T-shirt", "Sweater"]
want = input("What do you want (C, R, U, D)?")
if want == "R":
    print(Our_items)
elif want == "C":
    new_items =(input("Enter new items:"))
    Our_items.append(new_items)
    print(Our_items)
elif want == "D":
    delete_positions =int(input("Enter delete positions:"))
    del Our_items[delete_positions]
elif want == "U":
    update_positions =int(input("Enter update positions:"))
    updated_positions = (input("Enter updated positions:"))
    Our_items[update_positions] = updated_positions
    print(Our_items)








