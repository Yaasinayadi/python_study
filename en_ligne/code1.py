class Personne:
    def __init__(self, nom, age,email):
        self.nom = nom
        self.age = age
        self.email = email
    def se_presenter(self):
        print(f"Nom: {self.nom} | age: {self.age} | email: {self.email}")


personne1 = Personne("yassine", 25, "yass@gmail.com")
print(f"Nom: {personne1.nom}")
print(f"Nom: {personne1.age}")
print(f"Nom: {personne1.email}")


personne1.nom = 'yassine ayadi'
personne1.age += 1
personne1.email = 'yass.ayadi@gmail.com'

print(f"Nom: {personne1.nom}")
print(f"Nom: {personne1.age}")
print(f"Nom: {personne1.email}")

personne1.se_presenter()