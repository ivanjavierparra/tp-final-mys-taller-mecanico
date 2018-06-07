class Mecanico:
    """
    Clase que representa el mecanico
    """
    def __init__(self):
        self.disponible = True;

    def get_disponible(self):
    	return self.disponible

    def set_disponible(self, disponibilidad):
    	self.disponible = disponibilidad