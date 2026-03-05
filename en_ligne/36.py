class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher_infos(self):
        print(f"Nom: {self.nom}, Age: {self.age}")

class Salarie(Personne):
    def __init__(self, nom, age, numSum, salaire):
        Personne.__init__(self,nom, age) #herite de class parent
        self.numSum= numSum
        self.salaire = salaire

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Numero Somme: {self.numSum} | Salaire: {self.salaire}")

    def calculer_salaire(self):
        return self.salaire

class Etudiant(Personne):
    def __init__(self, nom, age, cne, notes):
        Personne.__init__(self,nom, age)
        self.cne = cne
        self.notes = notes # Liste de notes

    def afficher_infos(self):
        super().afficher_infos()
        print(f"CNE: {self.cne} | Notes: {self.notes}")

    def calculer_moyenne(self):
        if not self.notes:
            return 0
        return sum(self.notes) / len(self.notes)

class Doctorant(Salarie, Etudiant):
    def __init__(self, nom, age, numSum, salaire, cne, notes, departement, annee_inscri):
        Salarie.__init__(self, nom, age, numSum, salaire)
        Etudiant.__init__(self, nom, age, cne, notes)
        self.departement = departement
        self.annee_inscri = annee_inscri

    def afficher_infos(self):

        Salarie.afficher_infos(self)
        print(f"CNE (via Etudiant): {self.cne}")
        print(f"Département: {self.departement}, Année d'inscription: {self.annee_inscri}")

# Salarie
salarie = Salarie("Ali", 35, "H4256", 8000)
print("=== Salarie ===")
salarie.afficher_infos()
print("Salaire:", salarie.calculer_salaire())

#Etudiant 
etudiant = Etudiant("Kamal", 22, "E5456", [14, 16, 12, 15])
print("=== Etudiant ===")
etudiant.afficher_infos()
print("Moyenne:", etudiant.calculer_moyenne())

#doctorant
doctorant = Doctorant("Yassine", 28, "NS789", 6000, "CNE789", [15, 17, 16], "Informatique", 2024)
print("=== Doctorant ===")
doctorant.afficher_infos()
print("Moyenne:", doctorant.calculer_moyenne())
print("Salaire:", doctorant.calculer_salaire())