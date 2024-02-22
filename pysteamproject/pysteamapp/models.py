from django.db import models
import sqlite3  # Assuming you're using SQLite


# Create your models here.
class Jeu(models.Model):
    nom = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    img = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Bibliotheque(models.Model):
    nom = models.CharField(max_length=255)
    Jeu = models.ManyToManyField(Jeu, blank=True)
