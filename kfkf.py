from combat_round import combat_roundd, combat_full

player = {
    "NAME": "MAD",
    "CLASS": "TEACHER",
    "HP": 60,
    "STR": 7,
    "DEF": 10,
    "AGI": 1,
    "LVL": 1,
    "LUCK": 10,
}


cmd = input("Your command? ")

if cmd == "stats":
    print("NAME:", player["NAME"])
    print("CLASS:", player["CLASS"])
    print("HP:", player["HP"])
    print("STR:", player["STR"])
    print("DEF:", player["DEF"])
    print("LVL:", player["LVL"])
elif cmd == "here":
    print("Bạn đang ở trước cửa TechKids")
    print("Bạn có 2 lựa chọn")
    print("1. Về TechKids")
    print("2. Đi vào cánh rừng đối diện")
    option = input("Lựa chọn của bạn? ")
    if option == "1":
        print("Xin lỗi, đã hết giờ làm việc")
        print("Nhập lại đê!!!")
    elif option == "2":
        print("Bạn đã bước vào rừng")
        print("Bạn thấy một bình chất lỏng ở trên mặt đất")
        print("1. Bỏ qua")
        print("2. Nhặt lên uống")
        option = input("Lựa chọn của bạn? ")
        if option == "1":
            print("Tiếc quá")
        elif option == "2":
            player["HP"] = 100
            print("Bạn đã được hồi phục hoàn toàn HP")
            print("HP:", player["HP"])

        print("Bạn gặp 1 con Orc chưa trưởng thành")
        print("Bạn sẽ:")
        print("1. Chạy trốn")
        print("2. Nấp vào hang đá bên cạnh")
        print("3. ĐÁNH!")
        option = input("Lựa chọn của bạn?")
        if option == "1":
            print("Do bạn chạy quá chậm nên đã bị Orc bắt đi")
        elif option == "2":
            print("Con Orc không nhìn thấy bạn và bỏ đi")
            print("Tuy nhiên, khi bạn quay lại nhìn vào trong hang, bạn thấy một đàn sói")
        elif option == "3":
            orc = {
                "NAME": "SMALL ORC",
                "CLASS": "ORC",
                "STR": 1,
                "DEF": 2,
                "HP": 10,
                "LUCK": 2,
            }

            print("OPPONENT:", orc["NAME"])
            print("CLASS:", orc["STR"])
            print("STR:", orc["STR"])
            print("DEF:", orc["DEF"])
            print("HP:", orc["HP"])

            combat_full(player, orc)
            while True:
                combat_roundd(player, orc)
                if orc["HP"] <= 0:
                    break

                combat_roundd(orc, player)

                if player["HP"] <= 0:
                    break

                print("Bạn muốn:")
                print("1. Đánh tiếp")
                print("2. Chạy")
                print("3. Tự động đánh")
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

            damage = player["STR"] - orc["DEF"]
            if damage > 0:
                orc["HP"] -= damage
                print("Orc vừa mất", damage, "HP")

            damage = orc["STR"] - player["DEF"]
            if damage > 0:
                player["HP"] -= damage
                print("Player vừa mất", damage, "HP")
            else:
                print("Player không làm sao cả")



else:
    print("Nhập lại đê!!!")