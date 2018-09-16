from random import choice
items = []

def show_items():


def item_after_combat():
    new_item = generate_item()
    print("Một", new_item["NAME"], "vừa rơi ra")
    while True:
        print("1. Xem")
        print("2. Nhặt")
        print("3. Bỏ qua")
        option = input(">>>")
        if option == "1":
            show_item(new_item)
        if option == "2":
            print("Bạn đã nhặt", new_item['NAME'], "vào hòm đồ")
            add_item(new_item)
            count_items()
            break
        elif option == "3":
            print("Bạn đã bỏ qua món đồ")
            break


def add_item(item):
    items.append(item)


def count_items():
    count = len(items)
    print("Bạn có", count, "đồ trong hòm")


food_types = [
    "bánh bao",
    "cơm",
    "mỳ",
    "tôm"
]

cook_types = [
    "hấp",
    "chiên",
    "luộc",
    "rán"
]

food_levels = [
    "bình dân",
    "cao cấp",
    "xa xỉ",
    "hoàng gia"
]

def generate_item_name():
    f = choice(food_types)
    c = choice(cook_types)
    l = choice(food_levels)
    item_name = f + " " + c + " " + l
    return item_name


def generate_item():
    name = generate_item_name()
    item = {
        "NAME": name,
        "AGI": 3,
        "HP" : -1,
        "DEF": 2,
        "STR": 2,
    }
    return item


def show_item(game_item):
    print("*" * 20)

    for key, value in game_item.items():
        print("*", key, ":", value)

    print("*" * 20)



# steel_gaulet = {
#     "NAME": "STEEL_GAULET",
#     "STR": 100,
#     "SPEED": 50,
# }
#
# bronze_shield = {
#     "NAME": "BRONZE_SHIELD",
#     "DEF": 150,
#     "SPEED": -50,
# }
#
# golden_stick = {
#     "NAME": "GOLDEN_STICK",
#     "AGI": 15,
#     "HP": 20,
#     "ATK": 100
# }
#
#
# inventory = [steel_gaulet, bronze_shield, golden_stick]
# for item in inventory:
#     show_item(item)
#
