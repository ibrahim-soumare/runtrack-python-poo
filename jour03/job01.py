class Ville:
    def __init__(self, nom, habitants):
        self.nom = nom
        self._habitants = habitants  

    def get_habitants(self):
        return self._habitants

    def ajouter_population(self):
        self._habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def ajouter_population(self):
        self.ville.ajouter_population()


ville_paris = Ville("Paris", 1000000)
print("Nombre d'habitants de la ville de Paris:", ville_paris.get_habitants())

ville_marseille = Ville("Marseille", 861635)
print("Nombre d'habitants de la ville de Marseille:", ville_marseille.get_habitants())

john = Personne("John", 45, ville_paris)
myrtille = Personne("Myrtille", 4, ville_paris)
chloe = Personne("Chloé", 18, ville_marseille)

john.ajouter_population()
myrtille.ajouter_population()
chloe.ajouter_population()

print("Nombre d'habitants de la ville de Paris après l'arrivée de John et Myrtille:", ville_paris.get_habitants())
print("Nombre d'habitants de la ville de Marseille après l'arrivée de Chloé:", ville_marseille.get_habitants())