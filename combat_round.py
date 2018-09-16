from random import randint
from inventories import generate_item, show_item, count_items,add_item, item_after_combat
# player = {
#     "NAME": "PLAYER",
#     "ATK": 55,
#     "DEF": 30,
#     "HP": 100,
#     "INT": 90
# }
#
# orc = {
#     "NAME": "ORC",
#     "ATK": 60,
#     "DEF": 20,
#     "HP": 140,
#     "INT": 50
# }




def calculate_crit(player):
    has_crit = False
    dice = randint(0, 10)
    chance = player["LUCK"] + player["AGI"]
    if chance > dice:
        has_crit = True

    return has_crit

def combat_round(attacker, defender):
    print(attacker["NAME"], "is beating", defender["NAME"])
    calculate_crit(attacker)
    has_crit = calculate_crit(attacker)

    if has_crit:
        print("Đòn chí mạng")
        damage = attacker["STR"] * 2 - defender["DEF"]
    else:
        damage = attacker["STR"] - defender["DEF"]
    if damage > 0:
        defender["HP"] -= damage
        print(defender["NAME"], "lost", damage, "HP")
    else:
        attacker["HP"] -= abs(damage)
        print(attacker["NAME"], "lost", abs(damage), "HP")



def combat_full(player , opponent):
    while True:
        print("Bạn muốn:")
        print("1. Đánh tiếp")
        print("2. Chạy")
        print("3. Sử dụng đồ")
        print("4. Tự động đánh")
        option = input(">>>")

        if option == "1":
            print("Nhào zô")
        elif option == "2":
            from random import randint
            dice = randint(0, 100)
            if player["LUCK"] > dice:
                print("Bạn đã chạy thoát")
                break
            else:
                print("Chạy ko thành công, quay trở lại.")
        elif option == "3":
            print("BTVN")
        if player["HP"] <= 0:
            print("Bạn đã thua rồi, huhu")
        else:
            print(opponent["NAME"], "đã bị tiêu diệt")
            item_after_combat()





# while True:
#     combat(player, orc)
#     if orc["HP"] <= 0 or player["HP"] <= 0:
#         break
#     combat(orc, player)
#     if orc["HP"] <= 0 or player["HP"] <= 0:
#         break
# if player["HP"] >= 0:
#     print("orc died")
# elif orc["HP"] >= 0:
#     print("player lost")



