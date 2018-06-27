class Mecanico:
    """
    Clase que representa el mecanico
    """
    def __init__(self,dias):
        self.disponible = True
        self.dias = dias
        self.tiempo_uso_dia = [0] * self.dias
        

    def get_disponible(self):
    	return self.disponible

    def set_disponible(self, disponibilidad):
    	self.disponible = disponibilidad
    
    def get_tiempo_uso_dia(self):
        return self.tiempo_uso_dia

    def set_valor_arreglo(self,dia,valor):
        self.tiempo_uso_dia[dia] += valor