import interrupcion

class CPU:
    def __init__ (self, memoria,scheduler):
        self.enCpu = None
        self.pc = None
        self.pcFin = None
        self.idDeProceso = 0
        self.memoria = memoria
        self.handler = None
        self.modoUsuario = True
        self.modoKernel = False
        self.contador = 0
        self.cantDeTicks = 2
        self.scheduler = scheduler
        
    def cargarHandler(self, handler):
        self.handler = handler

    def cargar(self, pcb):
        self.enCpu = pcb
        self.pc = pcb.getPc()
        self.pcFin = pcb.getPcFin()
        self.idDeProceso = pcb.getPid()

    def liberar(self):
        self.enCpu = None
        self.pc = None

    def estaCargada(self):
        print (self.enCpu != None)
        return (self.enCpu != None)
        
    def modoKernel(self):
        self.modoUsuario = False
        self.modoKernel = True
        
    def modoUsuario(self):
        self.modoUsuario = True
        self.modoKernel = False

    def esModoUsuario(self):
        return self.modoUsuario

    def ejecutarInstruccionEnDirMemoria(self, pc):
        self.memoria.getInstruccion(pc).run()

    def tick(self):
        self.run()

    def run(self):
        if(self.esModoUsuario()):
            if ((self.enCpu != None) and (self.cantDeTicks != self.contador)): 
                self.ejecutarInstruccionEnDirMemoria(self.pc)
                self.aumenterPcYContador
            else:
                if(self.cantDeTicks == self.contador):
                    self.enCpu.setPc(self.pc)
                    self.handler.agarrarInterrupcion(interrupcion.IRQ(self.enCpu, interrupcion.IRQTipo.TIMEOUT))

            if((self.pcFin == self.pc) and self.esModoUsuario() and (self.enCpu != None)):
                self.handler.agarrarInterrupcion(interrupcion.IRQ(self.enCpu, interrupcion.IRQTipo.KILL))
            else:
                self.cargarcpu()

    def cargarcpu(self):
        if(self.scheduler.hayElementos()):
            pcb = self.scheduler.run()
            self.cargar(pcb)

    def aumenterPcYContador(self):
        self.pc = self.pc +1
        self.contador = self.contador +1
            