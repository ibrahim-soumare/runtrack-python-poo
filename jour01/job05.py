class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"La coordonnée horizontale x : {self.x}")

    def afficherY(self):
        print(f"La coordonnée verticale y : {self.y}")

    def changerX(self, x):
        self.x = x

    def changerY(self, y):
        self.y = y


point1 = Point(2, 3)

point1.afficherLesPoints()

point1.afficherX()
point1.afficherY()

point1.changerX(5)
point1.changerY(8)

point1.afficherLesPoints()