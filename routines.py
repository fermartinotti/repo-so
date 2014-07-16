class Routine:
	def __init__(self, cpu):
		self.cpu = cpu
		
	def run(self):
		pass

class KillRoutine(Routine):
	def __init__(self, cpu, scheduler):
		Routine.__init__(self, cpu)
		self.scheduler = scheduler
		
	def run(self):
		self.cpu.modoKernel()
		self.cpu.liberar()
		self.cpu.modoUsuario()
		self.cpu.cargar(self.scheduler.run())
		#self.cpu.run()

class TimeOutRoutine(Routine):
	def __init__(self, cpu, colaReady, scheduler):
		Routine.__init__(self, cpu)
		self.scheduler = scheduler
		self.cola = colaReady
		self.pcb = None
		#self.proximoPcb = self.scheduler.run()
		self.proximoPcb = None
		
	def cargarProximoPcb(self):
		self.proximoPcb = self.scheduler.run()
		
	def setPcb(self, irq):
		self.pcb = irq.getPcb()		
		
	def run(self):
		#self.cpu.modoKernel()
		self.cola.agregarPcb(self.pcb)
		self.cpu.liberar()
		self.cargarProximoPcb()
		self.cpu.cargar(self.proximoPcb)
		#self.cpu.modoUsuario()
		#self.cpu.run()

class NewPcbRoutine(Routine):
	def __init__(self, cpu):
		Routine.__init__(self, cpu)
		self.cola = None
		self.pcb = None
	
	def setPcb(self, irq):
		self.pcb = irq.getPcb()
		
	def setColaReady(self, colaReady):
		self.cola = colaReady	
	
	def run(self):
		self.cpu.modoKernel()
		self.cola.agregarPcb(self.pcb)
		self.cpu.modoUsuario()

class IORoutine(Routine):
	def __init__(self, cpu):
		Routine.__init__(self, cpu)
		self.waiting = None
		self.pcb = None
		
	def setPcb(self, irq):
		self.pcb = irq.getPcb()
		
	def setColaWaiting(self, colaWaiting):
		self.waiting = colaWaiting	

	def run(self):
		self.cpu.modoKernel()
		self.cpu.liberar()
		self.colaWaiting.agregarPcb(self.pcb)
		self.cpu.modoUsuario()
		self.cpu.run()
	
#class I(routine):
