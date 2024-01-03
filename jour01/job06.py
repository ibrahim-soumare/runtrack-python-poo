class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom


mon_animal = Animal()

print(f"Age de l'animal : {mon_animal.age}ans")

mon_animal.vieillir()

print(f"Age de l'animal après avoir vieilli : {mon_animal.age}ans")

mon_animal.nommer("L'animal se nomme Fido")

print(f"Nom de l'animal : {mon_animal.prenom}")