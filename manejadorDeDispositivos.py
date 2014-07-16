import manejadorDeMemoria, pcb

class ManejadorDeDispositivos:
    def __init__(self, memoria, disco):
        self.manejadorDeMemoria = manejadorDeMemoria.ManejadorDeMemoria(memoria)
        self.discoRigido = disco
        
    def cargarEstrategiaDeMemoria(self, estrategia):
        self.manejadorDeMemoria.cargarEstrategia(estrategia)
        
    def ejecutarPrograma(self, nombreProg):
        # Obtengo el programa del disco
        prog = self.discoRigido.buscar(nombreProg)
        # Creo el PCB del programa
        pc = self.manejadorDeMemoria.ultimaDir()
        pcFin = pc + (prog.cantidadDeInstrucciones() -1)
        PCB = pcb.Pcb(pc, pcFin)
        # Lo cargo en Memoria
        self.manejadorDeMemoria.cargarPrograma(prog, PCB)
        
        return PCB
        