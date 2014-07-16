import instruccion, memoria, programa, cpu, disco, manejadorDeDispositivos, manejadorDeMemoria, handler, scheduler, clock

# Creamos instrucciones
i1= instruccion.Instruccion("primera")
i2= instruccion.Instruccion("segunda")
i3= instruccion.Instruccion("tercera")
i4= instruccion.Instruccion("cuarta")
# Creamos un programa y le agregamos nuestras instrucciones
miPrograma = programa.Programa("prueba")
miPrograma.agregarInstruccion(i1)
miPrograma.agregarInstruccion(i2)
miPrograma.agregarInstruccion(i3)
miPrograma.agregarInstruccion(i4)

miPrograma1 = programa.Programa("hola")
miPrograma1.agregarInstruccion(i1)
miPrograma1.agregarInstruccion(i2)

miPrograma2 = programa.Programa("chau")
miPrograma2.agregarInstruccion(i1)
miPrograma2.agregarInstruccion(i2)
miPrograma2.agregarInstruccion(i3)
miPrograma2.agregarInstruccion(i4)


# Creamos un disco duro y almacenamos nuestro programa
miDisco = disco.Disco()
miDisco.almacenar(miPrograma)
miDisco.almacenar(miPrograma1)
miDisco.almacenar(miPrograma2)
# Creamos una memoria fisica
miMemoria = memoria.Memoria()
# Creamos un manejador de dispositivos con nuestra memoria y disco duro
miManejador = manejadorDeDispositivos.ManejadorDeDispositivos(miMemoria, miDisco)
longMemoria = miMemoria.longuitud

# Cargamos la estrategia de Asignacion continua Primer ajuste
miEstrategia = manejadorDeMemoria.PrimerAjuste(longMemoria)
miManejador.cargarEstrategiaDeMemoria(miEstrategia)
# Ejecutamos el programa, esto hace que se busque en disco y se cargue a la memoria
miPcb = miManejador.ejecutarPrograma("prueba")

miPcb.setPid(1)
miPcb.setEstado("ready")
miPcb.setPrioridad(2)
######################################################
miPcb1 = miManejador.ejecutarPrograma("hola")

miPcb1.setPid(2)
miPcb1.setEstado("ready")
miPcb1.setPrioridad(1)
######################################################
miPcb2 = miManejador.ejecutarPrograma("chau")

miPcb2.setPid(3)
miPcb2.setEstado("ready")
miPcb2.setPrioridad(3)


# Creamos un scheduler
miScheduler = scheduler.Scheduler()
# Cargamos al scheduler el pcb
miScheduler.agregar(miPcb)

miScheduler.agregar(miPcb1)
miScheduler.agregar(miPcb2)

miScheduler.colaReady.imprimirCola()

#Linea de prueva
