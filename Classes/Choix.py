class Choix():
    def lister_options(temp_liste : list):
    # Lister/Enumerer les options
        for index, value in enumerate(temp_liste):
            print(f"{index+1}. {value}")

    # Spécifier l'option pour Quitter/Annuler
        print(f"{len(temp_liste)+1}. Confirmer")
        while True:
        # Choisir une des options
            try:
                print(f"Choisissez une option: [1-{len(temp_liste)+1}]")
                choice = int(input())
                break
            except ValueError:
                print("Veuillez saisir un nombre.")
        # Renvoyer le choix effectué pour utiliser dans une autre méthode
        return choice