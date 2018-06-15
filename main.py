import numpy as np
from modelo import Taller, Evento, Reparacion


DIAS_DE_SIMULACION = 30
#60 mintos por hora * las 10 horas laborales.
MINUTOS_DE_SIMULACION_POR_DIA = 600

""" EVENTOS """
LLEGA_VEHICULO = 1  #cuando llega un vehiculo al taller
FINALIZA_REPARACION = 2 #cuando finaliza la reparacion de un vehiculo
SALE_VEHICULO = 3   #cuando un vehiculo sale del taller
""" ------- """

def generar_cola_eventos_ordenada():
    """
    En este metodo vamos a generar la cola de eventos DIARIA
    que manejará el main
    Se utilizará numpy y las definiciones de desvio, media, etc.
    """
    pass

def get_evento_proximo(cola_eventos):
    if (len(cola_eventos) > 0):
        proximo_evento = cola_eventos[0]
        cola_eventos.remove(proximo_evento)
        return proximo_evento
    else:
        return None
    
def agregar_evento(cola_eventos, nuevo_evento):
    bisect.insort(cola_eventos, nuevo_evento)

def ejecutar_evento(un_evento, taller): # tambien puede llamarse ocurre_evento. No me convence ninguno de los 2 como nombre. piensen otro
        if (un_evento.get_tipo() == LLEGA_VEHICULO):
            pass
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
            pass

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