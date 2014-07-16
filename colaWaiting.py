from multiprocessing import Queue
class ColaWaiting:
	def __init__(self):
		self.pcbs = Queue()

	def agregarPcb(self, pcb):
		self.pcbs.put(pcb)

	def obtenerPcb(self):
		return self.pcbs.get
