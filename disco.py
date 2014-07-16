class Disco:
    def __init__(self):
        self.espacioEnDisco = {}

    def almacenar(self, programa):
        self.espacioEnDisco[programa.nombre] = programa

    def buscar(self, nombre):
        return self.espacioEnDisco[nombre]
    
    def borrar(self, nombre):
        self.espacioEnDisco.remove(nombre)