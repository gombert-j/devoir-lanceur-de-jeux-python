from Classes.Choix import Choix
class TagsManager:
    def __init__(self):
        self.__liste_tags = list()

    def new_tag(self, new_tag : str):
        new_tag = new_tag.lower()  # convert to lower case
        if(new_tag not in self.__liste_tags):
            self.__liste_tags.append(new_tag)
            print(f"Tag: {new_tag} ajouté avec succès")
        else: print(f"Tag: {new_tag} déjà existant")

    def inspect_tags(self):
        choice = Choix.lister_options(self.__liste_tags)
        return choice
    
    def get_tags(self):
        return self.__liste_tags
    
    def set_tags(self, tags):
        self.__liste_tags = tags