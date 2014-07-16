import handler, main

class Kernel:
    def __init__(self, cpu, scheduler, deviceManager):
        self.scheduler = scheduler
        self.cpu = cpu
        self.handler = handler.Handler(self.cpu, self.scheduler)
        self.deviceManager = deviceManager

        self.modoKernel = True
        self.modoUsuario = False

    def startUp(self):
        self.handler.setKernel(self)
        
    def ejecutarPrograma(self, nombreProg):
        self.deviceManager.ejecutarPrograma(nombreProg)
        
