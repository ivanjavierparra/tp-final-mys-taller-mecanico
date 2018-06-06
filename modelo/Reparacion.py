class Reparacion:
    """
    Clase que representa una reparacion
    """
    def __init__(self, un_auto, un_mecanico, un_elevador = None):
        self.un_auto = un_auto
        self.un_mecanico = un_mecanico
        self.un_elevador = un_elevador