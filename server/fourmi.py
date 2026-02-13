class Fourmi:
    def __init__(self, id, espece, position):
        self.id = id
        self.espece = espece
        self.position = position  # (x, y)
        self.energie = 100

    def mettre_a_jour(self):
        # Pour l’instant on enlève juste de l’énergie
        self.energie -= 1
