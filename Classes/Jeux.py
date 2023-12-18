class Jeux:
    def __repr__(self):
        return self.__nom

    def set_nom(self, nom : str):
        self.__nom = nom

    def set_tags(self, tags : list):
        self.__tags = tags
    
    def set_img(self, img : str):
        self.__chemin_image = img

    def check_game(self):
        messageTags = ""
        for tag in self.__tags:
            messageTags += f" - {tag}\n"
        print(f"-----------------------\nNom du jeu: {self}\nTags: {messageTags}\nImage: {self.__chemin_image}")
