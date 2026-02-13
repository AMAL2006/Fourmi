import time
import threading
from monde import Monde

class SimulationServer:
    def __init__(self):
        self.monde = Monde()
        self.running = False
        self.thread = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def run(self):
        while self.running:
            self.monde.mettre_a_jour()
            time.sleep(0.5)  
            