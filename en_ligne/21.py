class Personne:
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age
    def se_presenter(self):
        return f"je suis {self.nom} {self.prenom},j'ai {self.age} ans"


personne1 = Personne("jamal","aouni",20)
personne2 = Personne("ahmed","mosabi",21)
personne3 = Personne("fatah","jilali",19)
print(f"{personne1.se_presenter}")