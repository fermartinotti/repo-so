class Instruccion:
    def __init__(self,nombreTipo):
        self.contenido = "Tipo de Instruccion: " +nombreTipo

    def run(self):
        print(self.contenido +", me ejecuto!")
        
    def __str__(self):
        return self.contenido
        
