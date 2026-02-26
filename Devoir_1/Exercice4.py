number1 = float(input("nombre 1: "))
number2 = float(input("nombre 2: "))

print("""|====== Menu ======|
1. Addition
2. Soustraction
3. Multiplication
4. Division
""")
choose = int(input("Veuillez choisir l'operation: "))

result = None
match choose:
    case 1 : result = number1 + number2
    case 2 : result = number1 - number2
    case 3 : result = number1 * number2
    case 4 : 
        if number2 == 0:
            print("Devision sur zero impossible")
        else:
            result = number1 / number2
    case _:
        print("choisie un nbre dans le Menu")

if result is not None:
    print(f"Resultat est: {result}")