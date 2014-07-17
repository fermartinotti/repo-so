
import colaReady

class Scheduler:
    def __init__(self):
        self.colaReady = colaReady.ColaReady()

    def run(self):
        pcb = self.colaReady.devolverElemento()
        return pcb

    def agregar(self, pcb):
        self.colaReady.agregarPcb(pcb)

    def hayElementos(self):
    	self.colaReady.hayPcb()
