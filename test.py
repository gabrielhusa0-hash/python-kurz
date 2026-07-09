# BMI
height = float(input("Vložte svou výšku v metrech: "))
weight = float(input("Vložze svou váhu v kg: "))

bmi = weight / (height * height)

print(round(bmi, 1))

if bmi < 18.5:
    print(f"Váš BMI má hodnotu {round(bmi, 1)}, máte podváhu")
elif bmi < 24.9:
    print(f"Váš BMI má hodnotu {round(bmi, 1)}, jste v normálu")
elif bmi < 24.9:
    print(f"Váš BMI má hodnotu {round(bmi, 1)}, máte nadváhu")
elif bmi < 34.9:
    print(f"Váš BMI má hodnotu {round(bmi, 1)}, jste obézní")
else:
    print(f"Váš BMI má hodnotu {round(bmi, 1)}, máte extermní obézítu")