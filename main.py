import numpy as np
from modelo import Taller, Evento, Reparacion, Reloj, Vehiculo


DIAS_DE_SIMULACION = 30
#60 mintos por hora * las 10 horas laborales.
MINUTOS_DE_SIMULACION_POR_DIA = 600
PORCENTAJE_DE_AUTOS_CON_ELEVADOR = 70

""" EVENTOS """
LLEGA_VEHICULO = 1  #cuando llega un vehiculo al taller
FINALIZA_REPARACION = 2 #cuando finaliza la reparacion de un vehiculo
SALE_VEHICULO = 3   #cuando un vehiculo sale del taller
""" ------- """

def generar_cola_eventos_ordenada():
    lista_eventos = []
    """
    Variables necesarias de generar:
    * Eventos de llegadas de los autos(15 por dia con dist. Poisson y 70% requieren elevador)
    * A cada auto que llega le tengo que poner:
        * patente
        * usa_elevador * tiempo_reparacion(1hr Dist. Exponencial)
        * tiempo_total (1dia Dist. Exponencial)
    """

    for dia in range(DIAS_DE_SIMULACION):
        """
        Por cada dia debo generar los 15~ eventos teniendo en cuenta el los minutos de ese día
        """
        minutos_diarios_usados = []
        #Caluclo la cantidad de autos para este día
        cantidad_de_autos = np.random.poisson(15)
        #De esa cantidad utilizando el PORCENTAJE (70%) me quedo con la cantidad de autos que no requieren elevador
        cant_autos_usan_elevador = (cantidad_de_autos * PORCENTAJE_DE_AUTOS_CON_ELEVADOR)/100# TODO REVISAR
        #Itereo por la cantidad de autos que NO requieren elevador
        for auto in cantidad_de_autos - cant_autos_usan_elevador:
            #Primero le asigo un minto del dia
            minuto_de_ocurrencia_evento = np.random.randint(0,MINUTOS_DE_SIMULACION_POR_DIA)[0] + (dia * MINUTOS_DE_SIMULACION_POR_DIA)
            #Mientras el numero sea repetido genero un nuevo
            while minuto_de_ocurrencia_evento in minutos_diarios_usados:
                minuto_de_ocurrencia_evento = np.random.randint(0,MINUTOS_DE_SIMULACION_POR_DIA)[0] + (dia * MINUTOS_DE_SIMULACION_POR_DIA)
            #Cuando encuentro un minuto nuevo lo agrego a la lista para futuras comparaciones
            minutos_diarios_usados.append(minuto_de_ocurrencia_evento)
            #Calculamos el tiempo de permanencia del auto
            tiempo_permanencia = 2 #TODO FALTA CALCULAR
            #Genero el Vehiculo
            vehiculo = Vehiculo(minuto_de_ocurrencia_evento,False,tiempo_total=tiempo_permanencia)
            #Genereo el evento
            evento = Evento(LLEGA_VEHICULO,minuto_de_ocurrencia_evento,None,vehiculo)
            lista_eventos.append(evento)
        for auto in cant_autos_usan_elevador:
            #Primero le asigo un minto del dia
            minuto_de_ocurrencia_evento = np.random.randint(0,MINUTOS_DE_SIMULACION_POR_DIA)[0] + (dia * MINUTOS_DE_SIMULACION_POR_DIA)
            #Mientras el numero sea repetido genero un nuevo
            while minuto_de_ocurrencia_evento in minutos_diarios_usados:
                minuto_de_ocurrencia_evento = np.random.randint(0,MINUTOS_DE_SIMULACION_POR_DIA)[0] + (dia * MINUTOS_DE_SIMULACION_POR_DIA)
            #Cuando encuentro un minuto nuevo lo agrego a la lista para futuras comparaciones
            minutos_diarios_usados.append(minuto_de_ocurrencia_evento)
            #Calculamos el tiempo de permanencia del auto
            tiempo_permanencia = 2 #TODO FALTA CALCULAR
            #Calculamos el tiempo de uso del elvador del auto
            tiempo_reparacion = 3 #TODO FALTA CALCULAR
            #Genero el Vehiculo
            vehiculo = Vehiculo(minuto_de_ocurrencia_evento,True,reparacion=tiempo_reparacion,tiempo_total=tiempo_permanencia)
            #Genereo el evento
            evento = Evento(LLEGA_VEHICULO,minuto_de_ocurrencia_evento,None,vehiculo)
            lista_eventos.append(evento)
    return lista_eventos

    
def get_evento_proximo(cola_eventos):
    if (len(cola_eventos) > 0):
        proximo_evento = cola_eventos[0]
        cola_eventos.remove(proximo_evento)
        return proximo_evento
    else:
        return None
    
def agregar_evento(cola_eventos, nuevo_evento):
    bisect.insort(cola_eventos, nuevo_evento)

def ejecutar_evento(un_evento, taller, reloj, cola_eventos): # tambien puede llamarse ocurre_evento. No me convence ninguno de los 2 como nombre. piensen otro
        if (un_evento.get_tipo() == LLEGA_VEHICULO):
            if(!taller.get_galpon().esta_lleno()):
                vehiculo = evento.get_vehiculo()
                taller.ingresar_vehiculo(vehiculo)
                
                mecanico = taller.get_mecanico_libre()
                if(mecanico):
                    necesita_elevador = vehiculo.usa_elevador()

                    if(necesita_elevador):
                        elevador = taller.get_elevador_libre()
                        if(elevador):
                            vehiculo.set_tiempo_espera( (reloj.get_tiempo() - un_evento.get_tiempo()))
                            reparacion = taller.iniciar_reparacion(evento.get_vehiculo(), mecanico, elevador)
                            evento_nuevo = Evento(FINALIZA_REPARACION, (reloj.get_tiempo() + vehiculo.get_tiempo_reparacion()), reparacion, vehiculo) 
                            agregar_evento(cola_eventos, evento_nuevo)
                    else:
                        reparacion = taller.iniciar_reparacion(evento.get_vehiculo(), mecanico)
                        vehiculo.set_tiempo_espera( (reloj.get_tiempo() - un_evento.get_tiempo()))

                        t_reparacion = vehiculo.get_tiempo_total() - vehiculo.get_tiempo_espera()
                        vehiculo.set_tiempo_reparacion(t_reparacion)

                        tiempo_ocurrencia = reloj.get_tiempo() + vehiculo.get_tiempo_reparacion()
                        evento_nuevo = Evento(FINALIZA_REPARACION, tiempo_ocurrencia, reparacion, vehiculo) 

                        agregar_evento(cola_eventos, evento_nuevo)

                #rechazamos el vehiculo cuando no hay lugar en el galpon
                #contador se vehiculos rechazados

            
        elif(un_evento.get_tipo() == FINALIZA_REPARACION):
            reparacion = un_evento.get_reparacion()
            galpon = taller.get_galpon()
            if (reparacion.get_elevador()):
                #Libero al mecanico y elevador
                #Guardamos las reparaciones finalizadas?
            else:
                #Libero al mecanico y el auto se va del galpon
                galpon.salida_vehiculo(reparacion.get_vehiculo)
            #Creo nuevo evento de reparacion
                reparacion = Reparacion()
                vehiculo = galpon.get_vehiculo()
                reparacion.vehiculo = vehiculo
                reparacion.mecanico = taller.get_mecanico_libre()
                if (vehiculo.usa_elevador()):
                    reparacion.elevador = taller.get_elevador_libre()
                tiempo = 800
                evento = Evento(FINALIZA_REPARACION, tiempo, reparacion)
        else:
            # SALE_VEHICULO
            taller.egresar_vehiculo(un_evento.get_vehiculo())

        #ELIMINAR EVENTO DE LA LISTA

def main():

    #Se genera el reloj que guiará toda la simulación.
    reloj = Reloj()
    #Se genera la instancia de Taller.
    taller = Taller()
    #Generar la cola de eventos.
    cola_eventos = generar_cola_eventos_ordenada()

    while (True):
        #Obtenemos el evento correspondiente
        evento = get_evento_proximo(cola_eventos)
        #Adelantamos el reloj hasta el tiempo del proximo evento
        reloj.set_valor(evento.get_tiempo())        
        #Procesamos el evento
        if (reloj.get_valor() < DIAS_DE_SIMULACION * MINUTOS_DE_SIMULACION_POR_DIA):
            respuesta = ejecutar_evento(evento, taller)
            #Dada la respuesta definimos si hay que agregar
            #otro evento en la cola de eventos
            if respuesta:
                agregar_evento(cola_eventos,respuesta)
        else:
            break
        

if __name__ == '__main__':
    main()