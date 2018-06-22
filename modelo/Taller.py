#Importamos las librerias necesarias
import Vehiculo
import Mecanico
import Elevador
import Galpon
import Reparacion


class Taller:
    """
    Clase que representa el taller
    """
    def __init__(self, cantidad_mecanicos=3, cantidad_elevadores=3, galpon=Galpon(10), reparaciones=[]):
        
        self.mecanicos = []
        for i in range cantidad_mecanicos:
            self.mecanicos.append(Mecanico())

        self.elevadores = []
        for i in range(cantidad_elevadores):
            self.elevadores.append(Elevador())

        self.galpon = galpon

        self.reparaciones = reparaciones

    def get_elevador_libre(self):
        for un_elevador in self.elevadores:
            if(un_elevador.get_disponible()):
                return un_elevador
        return None

    def get_mecanico_libre(self):
        for un_mecanico in self.mecanicos:
            if(un_mecanico.get_disponible()):
                return un_mecanico
        return None

    def ingresar_vehiculo(self, un_vehiculo):
        self.galpon.ingreso_vehiculo(un_vehiculo)

    def egresar_vehiculo(self, un_vehiculo):
        self.galpon.salida_vehiculo(un_vehiculo)

    def iniciar_reparacion(self, un_vehiculo, un_mecanico, un_elevador=None):
        una_reparacion = Reparacion(un_vehiculo, un_mecanico, un_elevador)
        self.reparaciones.append(una_reparacion)
        un_mecanico.set_disponible(False) #Pasar mecanico a ocupado
        if (un_elevador != None):
            un_elevador.set_disponible(False) #Pasar elevador a ocupado
        return reparacion

    def finalizar_reparacion(self, una_reparacion):
        self.reparaciones.remove(una_reparacion)
        una_reparacion.get_mecanico().set_disponible(True) #Pasar mecanico a disponible
        if (una_reparacion.get_elevador() != None):
            una_reparacion.get_elevador().set_disponible(True) #Pasar elevador a disponible
        una_raparacion.__del__()

    def get_galpon(self):
        return self.galpon


    def actualizarEstadoGUI():
        #cantidad de autos en el galpon
        #cantidad de mecanicos ocupados
        #cantidad de mecanicos libres
        #cantidad de elevadores ocupados
        #cantidad de elevadores libres
        pass
