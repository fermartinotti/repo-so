
class Memoria:
    def __init__(self):
        lista = ListaDeBloques(BloqueDeMemoria(0, 19))
        self.bloquesLibres = lista
        self.bloques = lista
        self.longitud = 20
        self.estrategia = None
    
    def cargarPrograma(self, programa, pcb):
        instrucciones = programa.instrucciones
        self.estrategia.cargar(self, instrucciones, pcb)
    
    def longitud(self):
        return self.longitud
    
    def cargarEstrategia(self, estrategia):
        self.estrategia = estrategia

######################################################################
''' 
Estrategias de Memoria
- Asignacion Continua
- Paginacion
 '''
class AsignacionContinua:
    
    def cargar(self, memoria, instrucciones, pcb):
        longitud = len(instrucciones)
        if(self.entraEnMemoria(memoria, longitud)):
            if(self.hayBloqueDisponible(memoria, longitud)):
                nuevoBloqueUsado = self.elegirBloque(memoria, longitud, pcb)
                nuevoBloqueUsado.cargarInstrucciones(instrucciones)
                memoria.bloquesUsados.agregarBloque(nuevoBloqueUsado)
            else:
                self.compactar(memoria)
                nuevoBloqueUsado = self.elegirBloque(memoria, longitud, pcb)
                nuevoBloqueUsado.cargarInstrucciones(instrucciones)
                memoria.bloquesUsados.agregarBloque(nuevoBloqueUsado)
        else:
            ''' swapping '''

    def memoriaLibre(self, memoria):
        acum = 0
        bloque = memoria.bloquesLibres.bloqueInicial
        while (bloque != None):
            acum = acum + bloque.longitud()
            bloque = bloque.siguiente
        return acum
                     
    def compactarBloquesLibres(self, memoria):
        acum=0
        for b in memoria.bloquesLibres:
            acum = acum + b.longitud()
        dirFinal = 19
        dirInicial = dirFinal - acum
        bloqueNuevo = BloqueDeMemoria(dirInicial , dirFinal)
        memoria.bloquesLibres.bloqueInicial = bloqueNuevo
        memoria.bloquesLibres.bloquefinal = bloqueNuevo
        
        
    def compactarBloques(self, memoria):
        bloque = memoria.bloques.bloqueInicial
        while (bloque != None):
            movimientos = 0
            bloque.subir(movimientos)
            if(bloque.estaUsado()):
                movimientos = movimientos + bloque.longitud()
            bloque = bloque.siguiente()   
        
    def compactar(self, memoria):
        self.compactarBloques(memoria)
        self.compactarBloquesLibres(memoria)
        
    def partirBloqueLibre(self, memoria, bloqueLibre, espacioAOcupar, pcb):
        anterior = bloqueLibre.anterior
        siguiente = bloqueLibre.siguiente
        dirInicioNueva= bloqueLibre.inicio + espacioAOcupar
        dirFinalNueva=  bloqueLibre.fin
        ''' saco el bloqueLibre de la lista de bloues libres para despues de partirlo agregar la parte que me queda libre '''
        memoria.bloquesLibres.sacarBloque(bloqueLibre)
        ''' saco el bloqueLibre de la lista de todos los bloues para despues de partirlo agregar cada bloque resultante'''
        memoria.bloques.sacarBloque(bloqueLibre)
        '''creo un bloque libre con la diferencia y lo pongo en la lista de libres'''
        bloqueLibreNuevo = BloqueDeMemoria( dirInicioNueva, dirFinalNueva)
        bloqueLibreNuevo.cargarAnterior(anterior)
        bloqueLibreNuevo.cargarSiguiente(siguiente)
        ''' creo un bloque usado y lo agrego '''
        inicio = bloqueLibre.inicio
        fin = inicio + espacioAOcupar-1
        bloqueUsadoNuevo = BloqueDeMemoria(inicio , fin)
        ''' agrego el bloque libre que quedo a cada lista '''
        memoria.bloquesLibres.agregarBloque(bloqueLibreNuevo)
        memoria.bloques.agregarBloque(bloqueLibreNuevo)
        ''' asigno el bloque al pcb '''
        pcb.asignarBloque(bloqueUsadoNuevo)
        
        return bloqueUsadoNuevo
        
        '''class Paginacion(ManejadorDeMemoria): '''
        
    def entraEnMemoria(self, memoria, longitud):
        return self.memoriaLibre(memoria) >= longitud
    
    def hayBloqueDisponible(self, memoria, longitud):
        bloque = memoria.bloquesLibres.bloqueInicial
        while (bloque != None):
            if(bloque.longitud() >= longitud):
                return True
            bloque = bloque.siguiente
        return False           
                
                
class PrimerAjuste(AsignacionContinua):
        
    def elegirBloque(self, memoria, longitud, pcb):
        bloque = memoria.bloquesLibres.bloqueInicial
        nuevoBloqueUsado = None
        while (bloque != None):
            if(bloque.longitud() >= longitud):
                nuevoBloqueUsado = self.partirBloqueLibre(memoria, bloque, longitud, pcb)
                return nuevoBloqueUsado
            else:
                bloque = bloque.siguiente
     

''' ############################################################################################# '''      
class BloqueDeMemoria:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin
        self.anterior = None
        self.siguiente = None
        self.instrucciones = {}
        
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

    def longitud(self):
        return self.fin - self.inicio +1
    
    def estaUsado(self):
        return self.usado
    
    def cargarInstrucciones(self, instrucciones):
        self.instrucciones = instrucciones
    
    def subir(self, cantidad):
        self.inicio = self.inicio+cantidad
        self.fin = self.fin+cantidad
        
class ListaDeBloques:
    def __init__(self, BInicial):
        self.bloqueInicial = BInicial
        self.bloqueFinal = BInicial
        
    def agregarBloque(self, bloque):
        fin = bloque.fin
        b = self.bloqueInicial
        termine = False
        if(self.listaVacia()):
            self.bloqueInicial = bloque
            self.bloqueFinal = bloque
        else:
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
    
    def listaVacia(self):
        return self.bloqueInicial == None
''' ############################################################################################# '''     

m = Memoria()
print m.longitud
print m.bloquesLibres.bloqueInicial.longitud()