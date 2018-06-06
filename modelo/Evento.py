class Evento:
    """
    Clase que representa un evento
    """
    def __init__(self, un_tipo, un_tiempo, una_reparacion=None, un_vehiculo=None):
        self.tipo = un_tipo
        self.tiempo = un_tiempo
        self.reparacion = una_reparacion
        self.vehiculo = un_vehiculo
    
    def get_tipo(self):
        return self.tipo

    def get_tiempo(self):
        return self.tiempo

    def get_reparacion(self):
        return self.reparacion

    def get_vehiculo(self):
        return self.vehiculo