class CeldaEnvejecimiento:
    def __init__(self):
        self.nivel1 = []
        self.nivel2 = []
        self.nivel3 = []       
        
    def agregarPcb(self, pcb):
        self.nivel1.insert(0,pcb)

    def devolverUltimoNivel(self):
        return (self.nivel3)
    
    def envejecerPrimero(self):
        self.nivel3 = self.nivel2
        self.nivel2 = self.nivel1
        self.nivel1 = []

    def envejecer(self, nivel):
        self.nivel3 = self.nivel3+self.nivel2
        self.nivel2 = self.nivel1
        self.nivel1 = nivel

    def envejecerUltimo(self, nivel):
        self.nivel3 = self.nivel3+self.nivel2
        self.nivel2 = self.nivel1
        self.nivel1 = nivel

    def devolverUltimo(self):
        if (len(self.nivel3) != 0):
            return (self.nivel3.pop())
        if(len(self.nivel2) !=0):
            return (self.nuvel2.pop())
        return (self.nivel1.pop())
    ''' Siempre va a sacar un elemento en una celda que tiene elementos,
	    La logica del filtrado la realiza la cola al momento de 
	    hacer el llamado al metodo devolver '''

    def hayElemento(self):
        return (len(self.nivel3) != 0 or len(self.nivel2) != 0 or len(self.nivel1) != 0)
    
    def devolverNivel(self, nivel):
        if (nivel == 1 ):
            return (self.nivel1)
        if(nivel == 2):
            return (self.nivel2)
        if(nivel == 3):
            return (self.nivel3)

class ColaReady:
    def __init__(self):
        self.prioridades = {}
        self.cantPrio = 3
        self.prioridades[1]= CeldaEnvejecimiento()
        self.prioridades[2]= CeldaEnvejecimiento()
        self.prioridades[3]= CeldaEnvejecimiento()

    def agregarPcb(self, pcb):
        agregarA = pcb.getPrioridad()
        self.prioridades[agregarA].agregarPcb(pcb)

    def envejecer(self):
        ultimoNivel2 = self.prioridades[2].devolverUltimoNivel()
        ultimoNivel1 = self.prioridades[1].devolverUltimoNivel()
        self.prioridades[3].envejecerUltimo(ultimoNivel2)
        self.prioridades[2].envejecer(ultimoNivel1)
        self.prioridades[1].envejecerPrimero()
    
    def devolverElemento(self):
        prio = 3
        encontro = False
        while (prio >0 and encontro == False): 
            if(self.prioridades[prio].hayElemento()):
                encontro = True
                return self.prioridades[prio].devolverUltimo()
            prio = prio-1
            if (encontro == False):
                ''' exception '''

    def hayPcb(self):
        return (self.prioridades[3].hayElemento() or self.prioridades[2].hayElemento() or self.prioridades[1].hayElemento())
