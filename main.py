import instruccion, memoria, programa, cpu, disco, manejadorDeDispositivos, handler, scheduler, clock

# Creamos instrucciones
i1= instruccion.CPUInstruccion("primera")
i2= instruccion.CPUInstruccion("segunda")
i3= instruccion.CPUInstruccion("tercera")
i4= instruccion.IOInstruccion("cuarta")
# Creamos un programa y le agregamos nuestras instrucciones
miPrograma = programa.Programa("prueba")
miPrograma.agregarInstruccion(i1)
miPrograma.agregarInstruccion(i2)
miPrograma.agregarInstruccion(i3)
miPrograma.agregarInstruccion(i4)
# Creamos un disco duro y almacenamos nuestro programa
miDisco = disco.Disco()
miDisco.almacenar(miPrograma)
# Creamos una memoria fisica
miMemoria = memoria.Memoria()
# Creamos un manejador de dispositivos con nuestra memoria y disco duro
miManejador = manejadorDeDispositivos.ManejadorDeDispositivos(miMemoria, miDisco)
# Cargamos la estrategia de Asignacion continua Primer ajuste
miEstrategia = memoria.PrimerAjuste()
miMemoria.cargarEstrategia(miEstrategia)
# Ejecutamos el programa, esto hace que se busque en disco y se cargue a la memoria
miPcb = miManejador.ejecutarPrograma("prueba")


#miPcb.setPid(1)
#miPcb.setEstado("ready")
#miPcb.setPrioridad(2)
######################################################
# Creamos un scheduler
miScheduler = scheduler.Scheduler()
# Creamos un CPU
miCpu = cpu.CPU(miMemoria, miScheduler)

# Un handler que maneja mis interrupciones y se lo cargamos tambien a la CPU, los dos se conocen
miHandler = handler.Handler(miCpu, miScheduler)
miHandler.cargarLasInterrupcionesDelSistema()
# Cargamos al scheduler el pcb
#miScheduler.agregar(miPcb)

# Hacemos el el scheduler nos de un elemento y se lo cargamos al CPU
#miCpu.cargar(miScheduler.run())

#miCpu.cargarHandler(miHandler)

# Creamos un clock, al cual le cargamos nuestra CPU y lo hacemos correr
c = clock.Clock()
c.cargarObserver(miCpu)
c.run()
