from Classes.Jeux import Jeux
from Classes.Sauvegarde import SauvegardeJSON
from Classes.Tags import Tags, TagsManager
import sys

class Bibliotheque:
    def __init__(self, chemin):
        self.__liste_jeux = list()

        self.__chemin_bibliotheque = chemin
        self.__storage = SauvegardeJSON()
        self.__storage.load(self.__chemin_bibliotheque)

    def afficher_menu(self):
        choice = ""
        affichage_options = {1:"Ajouter un jeu", 2:"Supprimer un jeu", 3:"Liste des jeux", 4:"Quitter"}
        print("------------- BIENVENUE SUR PYSTEAM ------------------")
        # Afficher toutes les options
        for option, message in affichage_options.items():
            print(f"{option}. {message}")
        while True:
            try:
                print("Choisissez une option: ")
                choice = int(input())
                break
            except ValueError:
                print("Veuillez saisir un nombre.")
        if(choice == 1): self.new_game()
        if(choice == 2): self.del_game()
        if(choice == 3): self.inspect_game()
        if(choice == 4): sys.exit()

    def new_game(self):
        print("------------- NOUVEAU JEU ------------------\n Nom du jeu: ")
        temp_nom = input()
        print("Tags du jeu (séparés par des ';', ex: fun;mignon;multijoueur): ")
        temp_tags = input().split(";")
        print("Chemin absolu vers l'image: ")
        temp_image = input()

        nouveau_jeu = Jeux()
        nouveau_jeu.set_nom(temp_nom)
        nouveau_jeu.set_tags(temp_tags)
        nouveau_jeu.set_img(temp_image)

        self.__liste_jeux.append(nouveau_jeu)
        print(f"------------- {nouveau_jeu} ajouté à la liste ---------------")
        self.afficher_menu()
    
    def del_game(self):
        # Choisir un jeu dans la liste
        choice = self.list_games()
        if(choice <= len(self.__liste_jeux)):
            # Supprimer le jeu choisi
            print(f"Suppression de {self.__liste_jeux[choice-1]}...")
            del(self.__liste_jeux[choice-1])
            print("Jeu supprimé")
        # Annuler/Quitter
        if choice == len(self.__liste_jeux)+1: pass

        # Retour vers le menu
        self.afficher_menu()

    def inspect_game(self):
        # Choisir un jeu dans la liste
        choice = self.list_games()
        if(choice <= len(self.__liste_jeux)):
            # Inspecter le jeu choisi
            self.__liste_jeux[choice-1].check_game()
        # Annuler/Quitter
        if choice == len(self.__liste_jeux)+1: pass

        # Retour vers le menu
        self.afficher_menu()

    def list_games(self):
        print("------------- LISTE DES JEUX ------------------")

        # Lister/Enumerer les jeux
        for index, jeu in enumerate(self.__liste_jeux):
            print(f"{index+1}. {jeu}")

        # Spécifier l'option pour Quitter/Annuler
        print(f"{len(self.__liste_jeux)+1}. Quitter")
        while True:
            # Choisir un des jeux
            try:
                print(f"Choisissez un jeu: [1-{len(self.__liste_jeux)+1}]")
                choice = int(input())
                break
            except ValueError:
                print("Veuillez saisir un nombre.")
        # Renvoyer le choix effectué pour utiliser dans une autre méthode
        return choice