class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.nom} {self.prenom}"

personne1 = Personne("Doe", "John")
personne2 = Personne("Smith", "Jane")
personne3 = Personne("Dupont", "Pierre")

print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())