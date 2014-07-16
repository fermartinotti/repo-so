
class Usuario():
    def __init__(self, nombre, contra):
        self.nombre = nombre
        self.contra = contra
        self.tipo = UsuarioComun()
    
    def nombre(self):
        return self.nombre
    
    def contra(self):
        return self.contra
    
    def cargarContra(self, contra):
        self.contra= contra

    def esAdimistrador(self):
        return self.tipo.esAdministrador()

    def cargarAdministrador(self):
        self.tipo = UsuarioAdministrador()

class UsuarioComun(Usuario):
        
    def esAdministrador(self):
        return False
    
class UsuarioAdministrador(Usuario):

    def esAdministrador(self):
        return True