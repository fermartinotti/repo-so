class ManejadorDeMemoria:
    def __init__(self, memoria):
        self.memoria = memoria
        self.estrategia = None
        
    def longitudDeMemoria(self):
        return self.memoria.longuitud()
    
    def ultimaDir(self):
        return self.memoria.ultimaDir()
    
    def cargarPrograma(self, programa, pcb):
        self.memoria.cargarPrograma(programa) # Cargado en memoria Fisica
        self.estrategia.elegirBloque(programa.cantidadDeInstrucciones(), pcb) # Cargado en memoria logica
        
    def cargarEstrategia(self, estrategia):
        self.estrategia = estrategia

######################################################################
''' 
Estrategias de Memoria
- Asignacion Continua
- Paginacion
 '''
class AsignacionContinua:
    def __init__(self, longuitudDeMemoria):
        listaNueva = ListaDeBloques(BloqueDeMemoria(0, longuitudDeMemoria-1))
        self.bloquesLibres = listaNueva
        self.bloques = listaNueva
        self.pcb = None

#    def elegirBloque(self, longuitud):
#        pass

    def memoriaLibre(self):
        acum = 0
        bloque = self.bloquesLibres.bloqueInicial
        while (bloque != None):
            acum = acum + bloque.longuitud()
            bloque = bloque.siguiente
        return acum
    
    def entraEnAlgunBloque(self, longuitud):
        bloque = self.bloquesLibres.bloqueInicial
        while(bloque != None):
            if(bloque.longuitud() >= long):
                return True
            bloque = bloque.siguiente
        return False
                     
    def compactarBloquesLibres(self):
        acum=0
        for b in self.bloquesLibres:
            acum = acum + b.longuitud()
        dirFinal = 255
        dirInicial = dirFinal - acum
        bloqueNuevo = BloqueDeMemoria(dirInicial , dirFinal)
        self.bloquesLibres.bloqueInicial = bloqueNuevo
        self.bloquesLibres.bloquefinal = bloqueNuevo
        
        
    def compactarBloques(self):
        bloque = self.bloques.bloqueInicial
        while (bloque != None):
            movimientos = 0
            bloque.subir(movimientos)
            if(bloque.estaUsado()):
                movimientos = movimientos + bloque.longuitud()
            bloque = bloque.siguiente()   
        
    def compactar(self):
        self.compactarBloques()
        self.compactarBloquesLibres()
        
    def partirBloqueLibre(self, bloqueLibre, espacioAOcupar, pcb):
        anterior = bloqueLibre.anterior
        siguiente = bloqueLibre.siguiente
        dirInicioNueva= bloqueLibre.inicio + espacioAOcupar
        dirFinalNueva=  bloqueLibre.fin
        '''creo un bloque libre con la diferencia y lo pongo en la lista de libres'''
        bloqueLibreNuevo = BloqueDeMemoria( dirInicioNueva, dirFinalNueva)
        bloqueLibreNuevo.cargarAnterior(anterior)
        bloqueLibreNuevo.cargarSiguiente(siguiente)
        ''' creo un bloque usado y lo agrego '''
        inicio = bloqueLibre.inicio
        fin = inicio + espacioAOcupar-1
        bloqueUsadoNuevo = BloqueDeMemoria(inicio , fin)
        
        self.bloques.agregarBloque(bloqueUsadoNuevo)
        self.bloques.agregarBloque(bloqueLibreNuevo)
        if(self.bloques.hayUnSoloBloque()):
            self.bloques = ListaDeBloques(bloqueLibreNuevo)
        else:
            self.bloquesLibres.agregarBloque(bloqueLibreNuevo)
        
        pcb.asignarBloque(bloqueUsadoNuevo)
        
        '''class Paginacion(ManejadorDeMemoria): '''
        
    def entraEnMemoria(self, longuitud):
        return self.memoriaLibre() >= longuitud
    
    def agregarBloque(self, longuitud, pcb):
        if(self.entraEnMemoria(longuitud)):
            if(self.entraEnAlgunBloque(longuitud)):
                self.elegirBloque(longuitud, pcb)
            else:
                self.compactar()
                self.elegirBloque(longuitud, pcb)
        else:
            '''swapping'''
                
class PrimerAjuste(AsignacionContinua):
    def __init__(self, longuitudDeMemoria):
        AsignacionContinua.__init__(self, longuitudDeMemoria)

    def elegirBloque(self,longuitud, pcb):
        bloque = self.bloquesLibres.bloqueInicial
        while (bloque != None):
            if(bloque.longuitud() >= longuitud):
                self.partirBloqueLibre(bloque, longuitud, pcb)
                break
            else:
                bloque = bloque.siguiente

###############################################################################
class BloqueDeMemoria:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin
        self.anterior = None
        self.siguiente = None
        self.usado = False
        
    def inicio(self):
        return self.inicio
    
    def inicioCargar(self, direccion):
        self.inicio = direccion
        
    def fin(self):
        return self.fin
    
    def finCargar(self, direccion):
        self.fin(direccion)
        
    def siguiente(self):
        return self.siguiente
    
    def cargarSiguiente(self, bloque):
        self.siguiente = bloque
    
    def anterior(self):
        return self.anterior
    
    def cargarAnterior(self, bloque):
        self.anterior = bloque

    def longuitud(self):
        return self.fin - self.inicio +1
    
    def estaUsado(self):
        return self.usado
    
    def subir(self, cantidad):
        self.inicio = self.inicio+cantidad
        self.fin = self.fin+cantidad
        
class ListaDeBloques:
    def __init__(self,BInicial , bloqueInicial = None, bloqueFinal = None):
        self.bloqueInicial = BInicial
        self.bloqueFinal = BInicial
        
    def agregarBloque(self, bloque):
        fin = bloque.fin
        b = self.bloqueInicial
        termine = False
        if (self.vaPrimero(bloque)):
            self.colocarPimero(bloque)
            termine = True  
        if(self.esUltimoBloque(b)):
            self.colocarUltimo(bloque)
            termine = True
        else:          
            while ((b != None) and (termine != True) and not(self.esUltimoBloque(b))):
                if(b.siguiente.inicio > fin):
                    sig = b.siguiente
                    b.cargarSiguiente(bloque)
                    sig.cargarAnterior(bloque)
                    bloque.cargarAnterior(b)
                    bloque.cargarSiguiente(sig)
                    termine = True
                b= b.siguiente
        if (not termine):#Lo colocamos ultimo
            self.bloqueFinal.cargarSiguiente(bloque)
            bloque.cargarAnterior(self.bloqueFinal)
            bloque.cargarSiguiente(None)
            self.bloqueFinal = bloque
            
    def vaPrimero(self, bloque):
        return (self.bloqueInicial.inicio > bloque.fin)
    
    def esUltimoBloque(self, bloque):
        return (bloque.siguiente == None)
               
    def colocarPrimero(self, bloque):
        bloque.cargarSiguiente(self.bloqueInicial)
        self.bloqueInicial.cargarAnterior(bloque)
        bloque.cargarAnterior(None)
        self.bloqueInicial = bloque        
        
    def colocarUltimo(self, bloque):
        self.bloqueFinal.cargarSiguiente(bloque)
        bloque.cargarAnterior(self.bloqueFinal)
        bloque.cargarSiguiente(None)
        self.bloqueFinal = bloque
        
    def hayUnSoloBloque(self):
        return (self.bloqueInicial.anterior == None) and (self.bloqueFinal.siguiente == None)
        
                