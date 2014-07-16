class Programa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrucciones = []
        self.cantInstrucciones = 0

    def agregarInstruccion(self, i):
        self.instrucciones.append(i)
        
    def cantidadDeInstrucciones(self):
        return len(self.instrucciones)
    
    def __str__(self):
        return "Nombre:" + str(self.nombre) 
    
    def run(self):
        for i in self.instrucciones:
            i.run()
    


