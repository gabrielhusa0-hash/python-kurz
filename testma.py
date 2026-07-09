age = int(input("Jaký je tvůj věk?\n"))
remain = 90 - age 
months = 12 * remain
weeks = 52 * remain
days = 365 * remain
print(f"Zbývá ti {days} dnů,\n {weeks} týdnů,\n {months} měsíců\n respektive {remain} let")

