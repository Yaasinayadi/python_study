donnees = [
    ("Sara", "Math", 12, "G1"),
    ("Sara", "Info", 14, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Adam", "Chimie", 18, "G1"),
    ("Sara", "Math", 11, "G1"),
    ("Bouchra", "Info", "abc", "G2"),
    ("", "Math", 10, "G1"),
    ("Yassine", "Info", 22, "G2"),
    ("Ahmed", "Info", 13, "G2"),
    ("Adam", "Math", None, "G1"),
    ("Sara", "Chimie", 16, "G1"),
    ("Adam", "Info", 7, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Hana", "Physique", 15, "G3"),
    ("Hana", "Math", 8, "G3"),
]

def valider(enregistrement):
    nom, matiere, note, groupe = enregistrement

    if not nom or not matiere or not groupe:
        return (False, "L'un de nom, matiere ou groupe est vide")

    if not isinstance(note, (int, float)):
        return (False, f"Note {note} doit etre un float")
    if note < 0 or note > 20:
        return (False, f"Note {note} doit etre entre 0 et 20")
    
    return (True, "")

valides = []
erreurs = []
doublons_exact = set()

for ligne in donnees:
    
    if ligne in valides:
        doublons_exact.add(ligne)
        continue
    est_valide, message_erreur = valider(ligne)

    if est_valide:
        nom, matiere, note, groupe = ligne
        ligne_propre = (nom, matiere, float(note), groupe)
        valides.append(ligne_propre)
    else:
        info_error = {
            'title': ligne,
            'reason': message_erreur
        }
        erreurs.append(info_error)

print(f"Lignes valides: {len(valides)}")
print(f"Erreurs détectées: {len(erreurs)}")
print(f"Doublons trouvés: {len(doublons_exact)}")

print("\n--- Exemple d'erreurs ---")
for err in erreurs:
    print(err)

print("\n--- Les Doublons ---")
print(doublons_exact)

matieres_uniques = set()
notes_etudiants = {}
groupes_pedagogiques = {}

for ligne in valides:
    nom, matiere, note, groupe = ligne

    # Only matiere
    matieres_uniques.add(matiere)

    # Format:  { "Nom": { "Matiere": [Note1, Note2] } }
    if nom not in notes_etudiants:
        notes_etudiants[nom] = {}
    if matiere not in notes_etudiants[nom]:
        notes_etudiants[nom][matiere] = []

    notes_etudiants[nom][matiere].append(note)

    #Format: { "G1": {"Sara", "Adam"} }
    if groupe not in groupes_pedagogiques:
        groupes_pedagogiques[groupe] = set()
    
    groupes_pedagogiques[groupe].add(nom)

# Affichage:
print("\n--- 1. Matieres enseignees ---")
print(matieres_uniques)

print("\n--- 2. Exemple structure Etudiant ")
print(notes_etudiants.get("Sara"))

print("\n--- 3. Groupes Pedagogiques ---")
for grp, liste_eleves in groupes_pedagogiques.items():
    print(f"Groupe {grp}: {liste_eleves}")

# Statistics et moyenne
def somme_recursive(liste_notes):
    if len(liste_notes) == 0:
        return 0
    else:
        return liste_notes[0] + somme_recursive(liste_notes[1:]) # somme_recursive(liste_notes[1:]) = somme de reste

def calculer_moyenne(liste_notes):
    if not liste_notes:
        return 0
    total = somme_recursive(liste_notes)
    return total / len(liste_notes)

print("\n--- Bulletins ---")
for etudiant, dossier_matieres in notes_etudiants.items() :
    print(f"|---Bulltin de {etudiant}---|")

    toutes_les_notes_etudiant = []
    for matiere, liste_notes in dossier_matieres.items():
        moy_mat = calculer_moyenne(liste_notes)
        print(f"{matiere} : {moy_mat:.2f}/20")

        toutes_les_notes_etudiant.extend(liste_notes)
    
    moy_gen = calculer_moyenne(toutes_les_notes_etudiant)
    print(f"Moyenne Generale: {moy_gen:.2f}/20")
    print("\n============")

