import time
from server.server import SimulationServer

server = SimulationServer(tick_rate=1)
server.start()

time.sleep(5)

etat = server.get_etat()
print(etat)

server.stop()
