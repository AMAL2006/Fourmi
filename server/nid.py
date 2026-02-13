from .fourmi import Fourmi

class Nid:
    def __init__(self, id, espece, position):
        self.id = id
        self.espece = espece
        self.position = position
        self.stock = 0
        self.fourmis = []

    def creer_fourmi(self, id_fourmi):
        nouvelle_fourmi = Fourmi(
            id=id_fourmi,
            espece=self.espece,
            position=self.position
        )
        self.fourmis.append(nouvelle_fourmi)
        return nouvelle_fourmi
