import numpy as np
from modelo import Elevador, Evento, Galpon, Mecanico, Reloj, Reparacion, Taller, Vhiculo

colaEntrada = []
colaEventos = []

def main(argumentos):
    reloj = Reloj()
    galpon = Galpon()
    mecanico = Mecanico()
    reparacion = Reparacion()
    elevador = Elevador()

    generarColaEntrada(colaEntrada)

    while(10 >= reloj.get_valor() and reloj.get_valor =< 20)
        if (len(galpon.espacio) > 0 )
            if (mecanico.disponible)
                reparacion(galpon.espacio.first(), mecanico, elevador)
                colaEventos.append(evento)
        if (not galpon.esta_lleno)
            galpon.espacio.append(colaEntrada.first())
        //ejecutar Proximo Evento