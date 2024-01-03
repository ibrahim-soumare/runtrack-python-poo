class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}."

personne1 = Personne("Doe", "Luc")
personne2 = Personne("Smith", "Alicia")
personne3 = Personne("Dupont", "Pierre")

print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())