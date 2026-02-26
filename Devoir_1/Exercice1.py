age = int(input("Veuillez saisir l'age: "))

if age in range(0, 13):
    print("Enfant !")
elif age in range(13, 18):
    print("Adolescent !")
elif age in range(18, 65):
    print("Adult")
else:
    print("Senior")