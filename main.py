from server import SimulationServer
import time

server = SimulationServer()
server.start()

time.sleep(3)

etat = server.get_etat()
print(etat)

server.stop()
