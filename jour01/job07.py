class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

personnage1 = Personnage()

print(f"Position initiale : {personnage1.position()}")

personnage1.droite()
personnage1.bas()

print(f"Nouvelle position : {personnage1.position()}")
