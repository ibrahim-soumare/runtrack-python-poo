class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"Âge de la personne : {self.age} ans")

    def bonjour(self):
        print("Bonjour")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation d'une personne
personne = Personne()
personne.afficherAge()  # Affiche l'âge par défaut (14) en console

# Instanciation d'un élève
eleve = Eleve()
eleve.afficherAge()  # Affiche l'âge par défaut (14) de la personne en console

# Instanciation d'un élève
eleve = Eleve()
eleve.bonjour()  # Affiche "Hello" en console grâce à la méthode bonjour de la classe Personne
eleve.allerEnCours()  # Affiche "Je vais en cours" en console grâce à la méthode allerEnCours de la classe Eleve
eleve.modifierAge(15)  # Redéfinir l'âge de l'élève à 15 ans
eleve.afficherAge()  # Affiche le nouvel âge (15) en console

# Instanciation d'un professeur
professeur = Professeur(matiereEnseignee="Histoire", age=40)
professeur.bonjour()  # Affiche "Hello" en console grâce à la méthode bonjour de la classe Personne
professeur.enseigner()  # Affiche "Le cours va commencer" en console grâce à la méthode enseigner de la classe Professeur