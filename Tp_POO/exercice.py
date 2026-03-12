from abc import ABC, abstractmethod
from dataclasses import dataclass

class Boisson(ABC):
    @abstractmethod
    def cout(self):
        pass
    @abstractmethod
    def description(self):
        pass
    def __add__(self, other):
        return BoissonCombinee(self, other)

class Cafe(Boisson):
    def cout(self):
        return 2.0
    def description(self):
        return "Cafe simple"

class The(Boisson):
    def cout(self):
        return 1.5
    def description(self):
        return "Thé"
class BoissonCombinee(Boisson):
    def __init__(self, b1, b2):
        self.b1 = b1 
        self.b2 = b2 
    def cout(self):
        return self.b1.cout() + self.b2.cout()
    def description(self):
        return self.b1.description() + " + " + self.b2.description()
class DecorateurBoisson(Boisson):
    def __init__(self, boisson_a_decorer):
        self._boisson = boisson_a_decorer
    
class Lait(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.5
    def description(self):
        return self._boisson.description() + ", Lait"
class Sucre(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.2
    def description(self):
        return self._boisson.description() + ", Sucre"
class Caramel(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.8
    def description(self):
        return self._boisson.description() + ", Caramel"
# accumeler les boisons calculer les prix, l'affichage
@dataclass
class Client:
    nom: str
    numero: int 
    points_fidelite: int = 0 
class Commande:
    def __init__(self, client):
        self.client = client
        self.boissons = []
    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)
        print(f"Ajoute : {boisson.description()}")
    def calculer_total(self):
        total = 0.0
        for boison in self.boissons:
            total += boison.cout()
        return total
    def afficher_commande(self):
        print(f"Commande de:{self.client.nom}")
        if not self.boissons:
            print("Commande est vide !")
        else:
            for boisson in self.boissons :
                print(f"{boisson.description()}, {boisson.cout()}$")
        
        print("----------")
        total_a_payer = self.calculer_total()
        print(f"  PRIX TOTAL : {total_a_payer}€")
class CommandeSurPlace(Commande):
    def afficher_commande(self):
        super().afficher_commande()
        print(" Type : Commande sur Place")
class commandeEmporter(Commande):
    def afficher_commande(self):
        super().afficher_commande()
        print(" Type : Commande a emporter")
class Fidelite:
    def ajouter_points_fidelite(self, client, montant_cmd: float):
        client.points_fidelite += int(montant_cmd // 5)
        print(f" Ajout de X points de fidélité au client Y. Total: Z points. ")
class CommandeFidele(Commande, Fidelite):
    def afficher_commande(self):
        super().afficher_commande()
        print(" Commande Fidele")
    def calculer_total(self):
        total_base = super().calculer_total()
        self.ajouter_points_fidelite(self.client, total_base)
        return total_base

boisson1 = Cafe()
print(f"{boisson1.description()} coute {boisson1.cout()}$")

boisson2 = The()
print(f"{boisson2.description()} coute {boisson2.cout()}$")

mon_cafe = Cafe()
mon_cafe = Lait(mon_cafe)

mon_cafe = Sucre(mon_cafe)

mon_cafe = Caramel(mon_cafe)

print(f"Commande finale : {mon_cafe.description()}")
print(f"Prix total : {mon_cafe.cout()}$")

#----------
print("\n--- Test Combinaison ---")
cafe_sucre = Sucre(Cafe())
the_lait = Lait(The())

menu = cafe_sucre + the_lait

print(f"Menu :  {menu.description()}")
print(f"Prix total du menu: {menu.cout()}$")

#-------------
print("\n--- Test Commande ---")
client1 = Client("Sara", 101)

boisson_a = Sucre(Lait(Cafe()))
boisson_b = Caramel(The())

ma_commande = Commande(client1)
ma_commande.ajouter_boisson(boisson_a)
ma_commande.ajouter_boisson(boisson_b)

ma_commande.afficher_commande()

# Test des commandes

# --- 1. Commande Sur Place ---
client_alice = Client("Alice", 201)
cafe_lait_sucre = Sucre(Lait(Cafe()))
commande_sur_place = CommandeSurPlace(client_alice)
commande_sur_place.ajouter_boisson(cafe_lait_sucre)
commande_sur_place.afficher_commande()

# 2. Commande À Emporter ---
client_bob = Client("Bob", 202)
the_caramel = Caramel(The())
commande_emporter = commandeEmporter(client_bob)
commande_emporter.ajouter_boisson(the_caramel)
commande_emporter.afficher_commande()

#3. Commande Fidèle (Héritage Multiple) ---
client_charlie = Client("Charlie", 203, 10) 
print(f"\nPoints de fidélité de Charlie avant commande: {client_charlie.points_fidelite}")

menu_fidele = (Cafe() + The()) # Une boisson combinée
commande_fidele = CommandeFidele(client_charlie)
commande_fidele.ajouter_boisson(menu_fidele)


commande_fidele.afficher_commande()
print(f"Points de fidélité de Charlie après commande: {client_charlie.points_fidelite}")