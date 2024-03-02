from parameterized import parameterized
from django.db import DataError
from django.test import TestCase

from pysteamapp.models import Jeu, Bibliotheque


# Create your tests here.
class JeuTest(TestCase):
    # Test si un jeu est bien créé dans la BDD avec le bon nom
    def test_jeu_with_valid_name(self):
        expected_name = 'valid'
        actual = Jeu.objects.create(nom=expected_name)
        from_db = Jeu.objects.get(nom=actual.nom)
        self.assertEqual(expected_name, from_db.nom)

    # Test si un jeu n'est pas créé dans la BDD si le nom est invalide

    # def test_jeu_with_too_long_name(self):
    #    invalid_name = 'invalid' * 50
    #    with self.assertRaises(DataError):
    #        Jeu.objects.create(nom=invalid_name)

    # Test si un jeu sans tags est possible
    def test_jeu_0_tags(self):
        actual = Jeu.objects.create(nom='game with 0 tags')
        self.assertEqual(0, len(actual.tags))

    # Test si un jeu n'est pas créé dans la BDD si le nom est invalide
    # def test_biblio_with_too_long_name(self):
    #    invalid_name = 'invalid' * 50
    #    with self.assertRaises(DataError):
    #        Bibliotheque.objects.create(nom=invalid_name)

    # test n Jeux dans l'instance de Bibliotheque
    @parameterized.expand([
        (0,),
        (2,),
        (130,),
        (4,),
    ])
    def test_n_jeux_in_bibliotheque(self, nb_jeux):
        actual = Bibliotheque.objects.create(nom=f'bibliotheque avec {nb_jeux} jeux')
        for idx in range(nb_jeux):
            actual.jeux.create(nom=f'item{idx}', tags="", img="image.png")
        self.assertEqual(nb_jeux, actual.nb_jeux)
