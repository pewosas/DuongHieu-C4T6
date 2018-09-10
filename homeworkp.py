player = {
    "NAME": "PLAYER",
    "ATK": 55,
    "DEF": 30,
    "HP": 100,
    "INT": 90
}

orc = {
    "NAME": "ORC",
    "ATK": 60,
    "DEF": 20,
    "HP": 140,
    "INT": 50
}

print("You are on your adventure")
print("Suggest:")
print("1.GO AHEAD")
print("2.GO HOME")
cmd = input("Your choice:(1, 2)?")

if cmd == "1":
    print(".There are two ways.")
    print("1.THE FOREST")
    print("2.ROCKY ROAD")
    cmd = input("Your way:(1, 2)?")

    if cmd == "1":
        print("You go to THE FOREST.")
        print("You face ORC.")
        print("1.ATTACK")
        print("2.RUN AWAY")
        cmd = input("You want:(1, 2)?")



        if cmd == "1":
            def combat(attacker, defender):
                print(attacker["NAME"], "is beating", defender["NAME"])
                damage = attacker["ATK"] - defender["DEF"]
                if damage > 0:
                    defender["HP"] -= damage
                    print(defender["NAME"], "lost", damage, "HP")
                else:
                    attacker["HP"] -= abs(damage)
                    print(attacker["NAME"], "lost", abs(damage), "HP")

                while True:
                    combat(player, orc)
                    if orc["HP"] <= 0 or player["HP"] <= 0:
                        break
                    combat(orc, player)
                    if orc["HP"] <= 0 or player["HP"] <= 0:
                        break


            if player["HP"] >= 0:
                print("ORC was knocked out.")
                print("1.KILL")
                print("2.EXCUSE")
                cmd = input("Your choice:")

                if cmd == "1":
                    print("ORC was killed")
                    print("You continue your adventure")
                    print("HAPPY ENDING")

                elif cmd == "2":
                    print("ORC runs away")
                    print("You ")

            elif orc["HP"] >= 0:
                print("You was killed")
                print("BAD ENDING")

    elif cmd == "2":
        print("You run back to starting point")


elif cmd == "2":
    print("You go to rocky road")
    print("You are not ingenious")
    print("You DIED")
    print("GAME OVER")









