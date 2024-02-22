from django.db import models
import sqlite3  # Assuming you're using SQLite
import json
from abc import ABC, abstractmethod
import sys


# Create your models here.


class Jeux:
    def __init__(self):
        self.__chemin_image = None
        self.__tags = None
        self.__nom = None

    def __repr__(self):
        return self.__nom

    def set_nom(self, nom: str):
        self.__nom = nom

    def set_tags(self, tags: list):
        self.__tags = tags

    def set_img(self, img: str):
        self.__chemin_image = img

    def check_game(self):
        messageTags = ""
        for tag in self.__tags:
            messageTags += f" - {tag}\n"
        print(f"-----------------------\nNom du jeu: {self}\nTags: {messageTags}\nImage: {self.__chemin_image}")

    def to_dict(self):
        return {
            'nom': self.__nom,
            'tags': self.__tags,
            'img': self.__chemin_image
        }


class SauvegardeIO(ABC):
    @abstractmethod
    def save(self, fichier: str):
        pass

    @abstractmethod
    def load(self, fichier: str):
        pass


class SauvegardeJSON(SauvegardeIO):
    def save(self, fichier: str, data):
        # Sauvegarde dans JSON
        print(f"Sauvegarde JSON dans: {fichier}")
        with open(fichier, 'w') as f:
            json.dump(data, f)

    def load(self, fichier: str):
        # Lire JSON
        print(f"Lecture JSON dans: {fichier}")
        try:
            with open(fichier, 'r') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}

        # Parse the JSON data into game objects
        games = []
        for game_dict in data.get('games', []):
            game = Jeux()
            game.set_nom(game_dict['nom'])
            game.set_tags(game_dict['tags'])
            game.set_img(game_dict['img'])
            games.append(game)

        tags = data.get('tags', [])

        return games, tags


class SauvegardeDB(SauvegardeIO):
    def __init__(self, db_name='pysteam-database.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def save(self, fichier: str, data):
        # Convert your data to the appropriate format and save it to the database
        # This will depend on the structure of your database
        pass

    def load(self, fichier: str):
        # Load data from the database and convert it to the appropriate format
        # This will depend on the structure of your database
        pass


class TagsManager:
    def __init__(self):
        self.__liste_tags = list()

    def new_tag(self, new_tag: str):
        new_tag = new_tag.lower()  # convert to lower case
        if new_tag not in self.__liste_tags:
            self.__liste_tags.append(new_tag)
            print(f"Tag: {new_tag} ajouté avec succès")
        else:
            print(f"Tag: {new_tag} déjà existant")

    def inspect_tags(self):
        choice = Choix.lister_options(self.__liste_tags)
        return choice

    def get_tags(self):
        return self.__liste_tags

    def set_tags(self, tags):
        self.__liste_tags = tags


class Choix:
    def lister_options(self, temp_liste: list):
        # Lister/Enumerer les options
        for index, value in enumerate(temp_liste):
            print(f"{index + 1}. {value}")

        # Spécifier l'option pour Quitter/Annuler
        print(f"{len(temp_liste) + 1}. Confirmer")
        while True:
            # Choisir une des options
            try:
                print(f"Choisissez une option: [1-{len(temp_liste) + 1}]")
                choice = int(input())
                break
            except ValueError:
                print("Veuillez saisir un nombre.")
        # Renvoyer le choix effectué pour utiliser dans une autre méthode
        return choice


class Bibliotheque:
    def __init__(self, chemin):
        self.__liste_jeux = list()
        self.__tags = TagsManager()
        self.__chemin_bibliotheque = chemin
        self.__storage = SauvegardeJSON()
        self.__liste_jeux, tags = self.__storage.load(self.__chemin_bibliotheque)
        self.__tags.set_tags(tags)

    def afficher_menu(self):
        choice = ""
        affichage_options = {1: "Ajouter un jeu",
                             2: "Supprimer un jeu",
                             3: "Liste des jeux",
                             4: "Ajouter un tag",
                             5: "Supprimer un tag",
                             6: "Liste des tags",
                             7: "Changer le mode de stockage",
                             8: "Quitter"}
        fonctions_options = {1: self.new_game,
                             2: self.del_game,
                             3: self.inspect_game,
                             4: self.new_tag,
                             5: self.del_tag,
                             6: self.inspect_tags,
                             7: self.change_storage_mode}

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
        if (choice >= 1) and (choice <= len(fonctions_options)):
            fonctions_options[choice]()
        elif choice > len(fonctions_options):
            sys.exit()

    def new_game(self):
        print("------------- NOUVEAU JEU ------------------\n Nom du jeu: ")
        temp_nom = input()
        temp_tags = list()
        choice = ""
        while choice != len(self.__tags.get_tags()) + 1:
            print("------------- TAGS ------------------")
            if temp_tags:
                print("Tags actuels:")
            for tag in temp_tags:
                print(f" - {tag}")
            choice = self.__tags.inspect_tags()
            if len(self.__tags.get_tags()) + 1 > choice > 0:
                tag_choisi = self.__tags.get_tags()[choice - 1].lower()  # convert to lower case
                if tag_choisi not in temp_tags:
                    temp_tags.append(tag_choisi)
                else:
                    temp_tags.remove(tag_choisi)

        print("Chemin absolu vers l'image: ")
        temp_image = input()

        nouveau_jeu = Jeux()
        nouveau_jeu.set_nom(temp_nom)
        nouveau_jeu.set_tags(temp_tags)
        nouveau_jeu.set_img(temp_image)

        self.__liste_jeux.append(nouveau_jeu)
        print(f"------------- {nouveau_jeu} ajouté à la liste ---------------")
        self.save_info()
        self.afficher_menu()

    def del_game(self):
        print("------------- SUPPRIMER UN JEU ------------------")
        # Choisir un jeu dans la liste
        choice = Choix.lister_options(self.__liste_jeux)
        if choice <= len(self.__liste_jeux):
            # Supprimer le jeu choisi
            print(f"Suppression de {self.__liste_jeux[choice - 1]}...")
            del (self.__liste_jeux[choice - 1])
            print("Jeu supprimé")
        # Annuler/Quitter
        if choice == len(self.__liste_jeux) + 1:
            pass
        # Retour vers le menu
        self.save_info()
        self.afficher_menu()

    def inspect_game(self):
        print("------------- LISTE DES JEUX ------------------")
        # Choisir un jeu dans la liste
        choice = Choix.lister_options(self.__liste_jeux)
        if choice <= len(self.__liste_jeux):
            # Inspecter le jeu choisi
            self.__liste_jeux[choice - 1].check_game()
        # Annuler/Quitter
        if choice == len(self.__liste_jeux) + 1:
            pass

        # Retour vers le menu
        self.afficher_menu()

    def new_tag(self):
        print("------------- NOUVEAU TAG ------------------\n Nom du tag: ")
        temp_tag = str(input())
        self.__tags.new_tag(temp_tag)
        self.save_info()
        self.afficher_menu()

    def del_tag(self):
        print("------------- SUPPRIMER UN TAG ------------------")
        # Choisir un tag dans la liste
        choice = self.__tags.inspect_tags()
        if choice <= len(self.__tags.get_tags()):
            # Supprimer le tag choisi
            print(f"Suppression de {self.__tags.get_tags()[choice - 1]}...")
            del (self.__tags.get_tags()[choice - 1])
            print("Tag supprimé")
        # Annuler/Quitter
        if choice == len(self.__tags.get_tags()) + 1:
            pass
        self.save_info()
        self.afficher_menu()

    def inspect_tags(self):
        print("------------- LISTE DES TAGS ------------------")
        for tag in self.__tags.get_tags():
            print(f" - {tag}")
        if not self.__tags.get_tags():
            print("Pas de tags...")
        self.afficher_menu()

    def save_info(self):
        self.__storage.save(self.__chemin_bibliotheque,
                            {'games': [game.to_dict() for game in self.__liste_jeux], 'tags': self.__tags.get_tags()})

    def change_storage_mode(self):
        print("------------- CHANGER LE MODE DE STOCKAGE ------------------")
        print("1. JSON")
        print("2. Base de données")
        print("Choisissez une option: ")
        choice = int(input())
        if choice == 1:
            self.__storage = SauvegardeJSON()
        elif choice == 2:
            self.__storage = SauvegardeDB()
        else:
            print("Option invalide")
        self.save_info()
        self.afficher_menu()
