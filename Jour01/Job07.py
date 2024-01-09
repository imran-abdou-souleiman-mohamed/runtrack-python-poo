class Personnage():
    def __init__(self):
        self.x = 300
        self.y = 100
    def gauche(self):
        self.x -= 15
    def droite(self):
        self.x += 15
    def bas(self):
        self.y += 15
    def haut(self):
        self.y -= 15
    def position(self):
        return (self.x, self.y)
n = Personnage()

n.bas()
n.droite()
n.bas()
n.droite()
print(n.position())