def get_etat(self):
    return {
        "nids": [
            {
                "id": nid.id,
                "position": nid.position,
                "stock": nid.stock
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
        "ressources": [
            {
                "position": r.position,
                "quantite": r.quantite
            }
            for r in self.ressources
        ]
    }
