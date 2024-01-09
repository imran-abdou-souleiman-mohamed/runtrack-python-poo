class Ville:
    def __init__(self, nom, nombre_habitants):
        self.nom = nom
        self._nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self._nombre_habitants

    def augmenter_population(self):
        self._nombre_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def ajouterPopulation(self):
        self.ville.augmenter_population()


paris = Ville("Paris", 1000000)

print(f"Population de la ville de Paris : {paris.get_nombre_habitants()}")

marseille = Ville("Marseille", 861635)

print(f"Population de la ville de Marseille : {marseille.get_nombre_habitants()}")


john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print(f"Mise a jour de la population de la ville de Paris : {paris.get_nombre_habitants()}")
print(f"Mise a jour de la population de la ville de Marseille : {marseille.get_nombre_habitants()}")