from abc import ABC, abstractmethod
from Classes.Jeux import Jeux

class SauvegardeIO(ABC):
    @abstractmethod
    def save(self, fichier : str):
        pass

    @abstractmethod
    def load(self, fichier : str):
        pass

import json

class SauvegardeJSON(SauvegardeIO):
    def save(self, fichier : str, data):
        # Sauvegarde dans JSON
        print(f"Sauvegarde JSON dans: {fichier}")
        with open(fichier, 'w') as f:
            json.dump(data, f)

    def load(self, fichier : str):
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

import sqlite3  # Assuming you're using SQLite

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