import time
from server.server import SimulationServer
from server.nid import Nid

server = SimulationServer(tick_rate=1)

# Création d’un nid
nid1 = Nid(id=1, espece="A", position=(5, 5))
server.monde.ajouter_nid(nid1)

# Création de 3 fourmis
for _ in range(3):
    server.monde.creer_fourmi_depuis_nid(nid1)

server.start()

time.sleep(5)

etat = server.get_etat()
print(etat)

server.stop()
