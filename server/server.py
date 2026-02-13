import threading
import time
from .monde import Monde

class SimulationServer:
    def __init__(self, tick_rate=0.5):
        self.monde = Monde()
        self.running = False
        self.tick_rate = tick_rate
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.run)
            self.thread.daemon = True  # s'arrête quand le programme s'arrête
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def run(self):
        while self.running:
            self.monde.mettre_a_jour()
            time.sleep(self.tick_rate)

    def get_etat(self):
        return self.monde.get_etat()
