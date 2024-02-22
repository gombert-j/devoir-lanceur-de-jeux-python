from Classes.JeuxBibliotheque import Bibliotheque
if __name__ == '__main__':
    pysteam = Bibliotheque("pysteam-library.json")
    pysteam.afficher_menu()