import os
password = "python123"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

saisie = ""
while saisie != password:
    saisie = input("Veuillez saisir un password: ")
    if saisie != password:
        clear_screen()
        print("Password Incorrect, try again !")
    
print(f"""Congratulations !
      Mot de passe correct, {password}""")
