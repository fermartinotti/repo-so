class IRQTipo:
	KILL = "Kill"
	TIMEOUT = "TimeOut"
	NEWPCB = "NewPcb"
	IO = "IO"
	RUNTIME = "RunTime"

class IRQ:
	def __init__(self, pcb, tipo):
		self.pcb = pcb
		self.tipo = tipo
	
	def getPcb(self):
		return self.pcb

	def getTipo(self):
		return self.tipo



