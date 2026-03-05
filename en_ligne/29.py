class Etudiant:
    def __init__(self):
        self.__cin = "XK220011"
        self.__cne = "M12121212"

    def afficher_prive(self):
        return self.__cin

sara = Etudiant()
print(sara._Etudiant__cin)
print(sara._Etudiant__cne)