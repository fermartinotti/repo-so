class Memoria():
    def __init__(self):
        self.memoria = {}
        self.ultimaDirCargada = 0
        self.longuitud = 20
    
    def cargarPrograma(self, programa):
        self.cargarInstrucciones(programa.instrucciones)

    def cargarInstrucciones(self,instr):
        for x in instr:
            self.memoria[self.ultimaDirCargada] = x
            self.ultimaDirCargada = self.ultimaDirCargada + 1
    
    def getInstruccion(self, direc):
        return self.memoria[direc] 
    
    def ultimaDir(self):
        return self.ultimaDirCargada
    
    def longuitud(self):
        return self.longuitud
