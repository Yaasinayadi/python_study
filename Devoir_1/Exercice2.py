import os
Contacts = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

run = True
while run:
    
    print("""|======Menu======|
1. Ajouter
2. Afficher
3. Quitter
""")
    try:
        choose = int(input("Veuillez saisir un choix: "))
    except ValueError:
        print("Veuillez entrer un nombre valide !")
        continue
    
    if choose == 1:
        clear_screen()
        nom = input("Veuillez saisir le nom du contact: ")
        Contacts.append(nom)
    elif choose == 2 :
        clear_screen()
        if len(Contacts) <= 0 :
            print("Liste des contacts Empty !")
        else:
            for i, contact in enumerate(Contacts):
                print(f"{i + 1} => {contact}")
    elif choose == 3 :
        print("Quitter...")
        run = False 
    else:
        clear_screen()
        print("Choix Invalide !")
       