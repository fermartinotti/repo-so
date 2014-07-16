'''
Created on 11/07/2014

@author: Equipo
'''
class Pcb:
    def __init__(self, pc, pcFin):
        self.pid = None
        self.pc = pc
        self.pcFin = pcFin
        self.estado = None
        self.prioridad = None
        self.bloqueDeMemoria = None


    def getPid(self):
        return self.pid
    
    def setPid(self, pid):
        self.pid = pid

    def getPc(self):
        return self.pc

    def setPc(self, pcNuevo):
        self.pc = pcNuevo

    def getPcFin(self):
        return self.pcFin

    def setPcFin(self, pcFin):
        self.pcFin = pcFin

    def setEstado(self, estado):
        self.estado = estado
        
    def getEstado(self):
        return self.estado
    
    def setPrioridad(self, prio):
        self.prioridad = prio

    def getPrioridad(self):
        return self.prioridad
    
    def asignarBloque(self, bloque):
        self.bloqueDeMemoria = bloque
    
class TablaPcb:
    def __init__(self):
        self.listaPcb = {}
        self.ultimoPid = 0

    def cargarPcb(self, pcb):
        self.listaPcb[self.ultimoPid] = pcb
        pcb.setPid(self.ultimoPid)
        self.ultimoPid += 1
