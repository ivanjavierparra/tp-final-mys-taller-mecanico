class Reparacion:
    """
    Clase que representa una reparacion
    """
    def __init__(self, un_vehiculo, un_mecanico, un_elevador = None):
        self.vehiculo = un_vehiculo
        self.mecanico = un_mecanico
        self.elevador = un_elevador
        
    def get_vehiculo(self):
        return self.vehiculo
    
    def get_mecanico(self):
        return self.mecanico
    
    def get_elevador(self):
        return self.elevador