from abc import ABC, abstractmethod
class SauvegardeIO(ABC):
    @abstractmethod
    def save(self, fichier : str):
        pass

    @abstractmethod
    def load(self, fichier : str):
        pass

class SauvegardeJSON(SauvegardeIO):
    def save(self, fichier : str):
        # Sauvegarde dans JSON
        print(f"Sauvegarde JSON dans: {fichier}")
        pass

    def load(self, fichier : str):
        # Lire JSON
        print(f"Lecture JSON dans: {fichier}")
        pass