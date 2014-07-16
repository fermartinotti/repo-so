import colaWaiting, colaReady, routines, interrupcion

class Handler:
    def __init__(self, cpu, scheduler):
        self.cpu = cpu
        self.scheduler = scheduler
        self.colaWaiting = colaWaiting.ColaWaiting()
        self.colaReady = colaReady.ColaReady()
        self.kernel = None
        self.interrupciones = {}        

    def setKernel(self, kernel):
        self.kernel = kernel

    #def registrarInterrupcion(self, interrup, interrupAlg):
    #    self.interrupciones[interrup.tipo] = interrupAlg
        
    def registrarInterrupcion(self, tipo, interrupAlg):
        self.interrupciones[tipo] = interrupAlg

    def agarrarInterrupcion(self, interrup):
        if(interrup.tipo == interrupcion.IRQTipo.KILL):
            self.interrupciones[interrup.tipo].run()
        if(interrup.tipo == interrupcion.IRQTipo.TIMEOUT):
            self.interrupciones[interrup.tipo].setPcb(interrup)
            self.interrupciones[interrup.tipo].run()
        if(interrup.tipo == interrupcion.IRQTipo.NEWPCB):
            self.interrupciones[interrup.tipo].setPcb(interrup)
            self.interrupciones[interrup.tipo].setColaReady(interrup)
            self.interrupciones[interrup.tipo].run()
        if(interrup.tipo == interrupcion.IRQTipo.IO):
            self.interrupciones[interrup.tipo].setPcb(interrup)
            self.interrupciones[interrup.tipo].setColaWaiting(interrup)
            self.interrupciones[interrup.tipo].run()
        
    def cargarLasInterrupcionesDelSistema(self):
        kill = routines.KillRoutine(self.cpu, self.scheduler)
        timeOut = routines.TimeOutRoutine(self.cpu, self.colaReady, self.scheduler)
        newPcb = routines.NewPcbRoutine(self.cpu)
        io = routines.IORoutine(self.cpu)
        
        self.registrarInterrupcion(interrupcion.IRQTipo.KILL, kill)
        self.registrarInterrupcion(interrupcion.IRQTipo.TIMEOUT, timeOut)
        self.registrarInterrupcion(interrupcion.IRQTipo.NEWPCB, newPcb)
        self.registrarInterrupcion(interrupcion.IRQTipo.IO, io)
        
        