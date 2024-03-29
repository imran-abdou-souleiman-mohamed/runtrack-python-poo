class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True  

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur

    def set_nb_pages(self, nouveau_nb_pages):
        if nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.__disponible:
            print("Emprunt du livre.")
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.__disponible:
            print("Rendu du livre.")
            self.__disponible = True
        else:
            print("Le livre n'a pas été emprunté, donc ne peut pas être rendu.")

mon_livre = Livre(titre="Harry Potter", auteur="J.K. Rowling", nb_pages=400)

print(f"Le livre est disponible : {mon_livre.verification()}")

mon_livre.emprunter()

mon_livre.rendre()

mon_livre.emprunter()

mon_livre.rendre()

print(f"Le livre est disponible : {mon_livre.verification()}")