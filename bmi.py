mass = float(input("Mass(kg) : "))
height = float(input("Height(m) : "))
bmi = mass/(height*height)
if bmi < 16:
    print("Severely underweight ")
elif bmi < 18.5:
    print("Underweight " )
elif bmi < 25:
    print("Normal " )
elif bmi < 30:
    print("Overweight " )
else:
    print("Obese ")