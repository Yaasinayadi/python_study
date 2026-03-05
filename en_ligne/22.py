class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometre = 0  # Valeur par défaut

#objet
ma_voiture = Voiture("mercedes", "E-250", 1993)

# Affichage
print("Marque :", ma_voiture.marque)
print("Modèle :", ma_voiture.modele)
print("Année :", ma_voiture.annee)
print("Kilométrage :", ma_voiture.kilometre)