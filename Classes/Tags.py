from Classes.Choix import Choix
class TagsManager:
    def __init__(self):
        self.__liste_tags = list()

    def new_tag(self, new_tag : str):
        liste = self.getTags()
        for tag in liste:
            if(new_tag != tag): 
                self.__liste_tags.append(new_tag)
                print(f"{new_tag} ajouté avec succès")
            else: print(f"{tag} déjà existant")

    def inspect_tags(self):
        Choix.lister_options(self.__liste_tags)

class Tags:
    def set_name(self, nom : str):
        self.__nomTag = nom