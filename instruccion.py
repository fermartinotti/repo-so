from time import sleep

class Instruccion:
    def __init__(self,nombre):
        self.contenido = nombre

    def run(self):
        print("not defined method")
        
class IOInstruccion(Instruccion):
    def __init__(self,nombre):
        Instruccion.__init__(self,nombre)
        
    def run(self):
        print("ejecutando la instruccion de I/O:")
        print(self.contenido)
        sleep(2)
        
class CPUInstruccion(Instruccion):
    def __init__(self,nombre):
        Instruccion.__init__(self,nombre)

    def run(self):
        print("ejecucion de: " + self.contenido)
