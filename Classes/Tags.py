from Classes.Choix import Choix
class TagsManager:
    def __init__(self):
        self.__liste_tags = list()

    def newTag(self, new_tag : str):
        liste = self.getTags()
        for tag in liste:
            if(new_tag != tag): 
                self.__liste_tags.append(new_tag)
                print(f"{new_tag} ajouté avec succès")
            else: print(f"{tag} déjà existant")

    def getTags(self):
        Choix.lister_options(self.__liste_tags)

class Tags:
    def setName(self, nom : str):
        self.__nomTag = nom