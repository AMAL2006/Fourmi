from .nid import Nid
from .fourmi import Fourmi
from .ressource import Ressource


class Monde:
    def __init__(self):
        self.nids = []
        self.fourmis = []
        self.ressources = []
        self.compteur_fourmis = 0

    def ajouter_nid(self, nid):
        self.nids.append(nid)

    def creer_fourmi_depuis_nid(self, nid):
        self.compteur_fourmis += 1
        fourmi = nid.creer_fourmi(self.compteur_fourmis)
        self.fourmis.append(fourmi)

    def retirer_fourmi(self, fourmi):
        if fourmi in self.fourmis:
            self.fourmis.remove(fourmi)

        for nid in self.nids:
            if fourmi in nid.fourmis:
                nid.fourmis.remove(fourmi)

    def mettre_a_jour(self):
        for f in self.fourmis[:]:
            f.mettre_a_jour()
            if f.energie <= 0:
                self.retirer_fourmi(f)

    def get_etat(self):
        return {
            "nids": [
                {
                    "id": nid.id,
                    "position": nid.position,
                    "stock": nid.stock,
                    "nb_fourmis": len(nid.fourmis)
                }
                for nid in self.nids
            ],
            "fourmis": [
                {
                    "id": f.id,
                    "espece": f.espece,
                    "position": f.position,
                    "energie": f.energie
                }
                for f in self.fourmis
            ],
        }
