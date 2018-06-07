#Importamos las librerias necesarias
import numpy as np
import bisect #utilizada para trabajar con listas ordenadas

import Vehiculo
import Mecanico
import Elevador
import Galpon
import Reparacion
import Evento
import Reloj

""" EVENTOS """
LLEGA_VEHICULO = 1  #cuando llega un vehiculo al taller
FINALIZA_REPARACION = 2 #cuando finaliza la reparacion de un vehiculo
SALE_VEHICULO = 3   #cuando un vehiculo sale del taller
""" ------- """


class Taller:
    """
    Clase que representa el taller
    """
    def __init__(self, lista_eventos=[], cantidad_mecanicos=3, cantidad_elevadores=3, galpon=Galpon(10), reparaciones=[]):
        self.eventos = lista_eventos
        self.eventos.sort()
        
        self.mecanicos = []
        for i in range cantidad_mecanicos:
            self.mecanicos.append(Mecanico())

        self.elevadores = []
        for i in range(cantidad_elevadores):
            self.elevadores.append(Elevador())

        self.galpon = galpon

        self.reparaciones = reparaciones

        self.reloj = Reloj()

        
    def get_evento_proximo(self):
        if (len(self.eventos) > 0):
            return seft.eventos[0]
        else:
            return None
        
    def agregar_evento(self, nuevo_evento):
        bisect.insort(self.eventos, nuevo_evento)

    def eliminar_evento(self, evento):
        self.eventos.remove(evento)

    def get_elevador_libre(self):
        for un_elevador in self.elevadores:
            if(un_elevador.get_disponible()):
                return un_elevador
        return None

    def get_mecanico_libre(self):
        for un_mecanico in self.mecanicos:
            if(un_mecanico.get_disponible()):
                return un_mecanico
        return = None

    def agregar_evento(self, un_evento):
        bisect.insort(self.eventos, un_evento)
        
    def remover_evento(self, un_evento):
        self.eventos.remove(un_evento)

    def ingresar_vehiculo(self, un_vehiculo):
        #
        pass

    def egresar_vehiculo(self, un_vehiculo):
        #
        pass

    def iniciar_reparacion(self, una_reparacion):
        #self.reparaciones.append(una_reparacion)
        #una_reparacion.get_mecanico().set_disponible(False) #Pasar mecanico a ocupado
        #if (una_reparacion.get_elevador() != None):
        #    una_reparacion.get_elevador().set_disponible(False) #Pasar elevador a ocupado
        pass

    def finalizar_reparacion(self, una_reparacion):
        #self.reparaciones.remove(una_reparacion)
        #una_reparacion.get_mecanico().set_disponible(True) #Pasar mecanico a disponible
        #if (una_reparacion.get_elevador() != None):
        #    una_reparacion.get_elevador().set_disponible(True) #Pasar elevador a disponible
        #una_raparacion.__del__()
        pass


    def ejecutar_evento(self, un_evento): # tambien puede llamarse ocurre_evento. No me convence ninguno de los 2 como nombre. piensen otro
        if (un_evento.get_tipo() == LLEGA_VEHICULO):
            pass
        elif(un_evento.get_tipo() == FINALIZA_REPARACION):
            pass
        else:
            pass

