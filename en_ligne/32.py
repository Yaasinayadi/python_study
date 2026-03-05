class Personne:
    def __init__(self, nom, age):
        self._nom = nom
        self._age = age

    @property
    def age(self):
        """Récupère la valeur de l'âge."""
        return self._age

    @age.setter
    def age(self, valeur):
        """Définit l'âge avec des contrôles de sécurité."""
        if not isinstance(valeur, int):
            raise TypeError("Entrez une val INT")
        if valeur < 0:
            raise ValueError("La val ne peut pas etre moins que 0")
        if valeur > 140:
            raise ValueError("L'Age ici est irrealiste")
        
        self._age = valeur

    def se_presenter(self):
        """Retourne une chaîne de présentation."""
        return f"Je suis {self._nom}, {self._age} ans"

personne1 = Personne("fatah", 15)
personne2 = Personne("moaud", 28)
personne3 = Personne("nissrine", 16)

print(personne1.se_presenter()) 
print(personne2.se_presenter()) 
print(personne3.se_presenter()) 

personne1.age = 30 
print(f"Nouvel âge de Sara : {personne1.age}")