print("Vítejte v kalkulátoru na výpočet plateb")
cost = int(input("Kolik máte celkem zaplatit? "))
percentage = int(input("Kolik chcete dát spropitného (v %). "))
people = int(input("Mezi kolika lidí se má rozdělit částka? "))

one_payment = (cost + ( cost * percentage / 100)) / people
final_payment = "{:+.2f}".format(one_payment)
print(f"Každý člověk by měl zaplatit {final_payment} Kč")

print("{:+.2f}".format(3.1415926));