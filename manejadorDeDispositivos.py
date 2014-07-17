import pcb, scheduler

class ManejadorDeDispositivos:
    def __init__(self, memoria, disco):
        self.memoria= memoria
        self.discoRigido = disco
        self.scheduler = scheduler.Scheduler()
        
    def ejecutarPrograma(self, nombreProg):
        # Obtengo el programa del disco
        prog = self.discoRigido.buscar(nombreProg)
        # Creo el PCB del programa
        PCB = pcb.Pcb()
        PCB.setPrioridad(1)
        # Lo cargo en Memoria
        self.memoria.cargarPrograma(prog, PCB)
        self.scheduler.agregar(PCB)
        
