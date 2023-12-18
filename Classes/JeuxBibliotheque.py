from Classes.Jeux import Jeux
from Classes.Sauvegarde import SauvegardeJSON
from Classes.Tags import TagsManager
from Classes.Choix import Choix
import sys

class Bibliotheque:
    def __init__(self, chemin):
        self.__liste_jeux = list()
        self.__tags = TagsManager()
        self.__chemin_bibliotheque = chemin
        self.__storage = SauvegardeJSON()
        self.__storage.load(self.__chemin_bibliotheque)

    def afficher_menu(self):
        choice = ""
        affichage_options = {1:"Ajouter un jeu", 
                             2:"Supprimer un jeu", 
                             3:"Liste des jeux", 
                             4:"Ajouter un tag", 
                             5:"Supprimer un tag", 
                             6:"Liste des tags", 
                             7:"Quitter"}
        fonctions_options = {1: self.new_game,
                             2: self.del_game,
                             3: self.inspect_game,
                             4: self.new_tag,
                             5: self.del_tag,
                             6: self.inspect_tags}
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
        if((choice >= 1) and (choice <= len(fonctions_options))): fonctions_options[choice]()
        else: sys.exit()

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
        print("------------- SUPPRIMER UN JEU ------------------")
        # Choisir un jeu dans la liste
        choice = Choix.lister_options(self.__liste_jeux)
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
        print("------------- LISTE DES JEUX ------------------")
        # Choisir un jeu dans la liste
        choice = Choix.lister_options(self.__liste_jeux)
        if(choice <= len(self.__liste_jeux)):
            # Inspecter le jeu choisi
            self.__liste_jeux[choice-1].check_game()
        # Annuler/Quitter
        if choice == len(self.__liste_jeux)+1: pass

        # Retour vers le menu
        self.afficher_menu()
    
    def new_tag(self):
        print("------------- NOUVEAU TAG ------------------\n Nom du tag: ")
        temp_tag = str(input())
        self.__tags.new_tag(temp_tag)
        self.afficher_menu()
    
    def del_tag(self):
        print("------------- SUPPRIMER UN TAG ------------------")
        # Choisir un tag dans la liste
        choice = self.__tags.inspect_tags()
        if(choice <= len(self.__tags.get_tags())):
            # Supprimer le tag choisi
            print(f"Suppression de {self.__tags.get_tags()[choice-1]}...")
            del(self.__tags.get_tags()[choice-1])
            print("Tag supprimé")
        # Annuler/Quitter
        if choice == len(self.__tags.get_tags())+1: pass

    def inspect_tags(self):
        choice = "" 
        while choice != len(self.__tags.get_tags())+1:
            choice = self.__tags.inspect_tags()
        self.afficher_menu()