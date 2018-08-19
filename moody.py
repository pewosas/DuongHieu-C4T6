from random import randint

mood = randint(0, 100)

if mood < 30:
    print(":(")
elif 30 < mood <60:
    print(".-.")
else:
    print(":)")




