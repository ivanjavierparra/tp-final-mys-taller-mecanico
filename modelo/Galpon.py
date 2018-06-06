class Galpon:
    """
    Clase que representa el Galpon
    """
    def __init__(self, capacidad):
        self.capacidad_max = capacidad;
        self.espacio = []
        
    def get_espacio_libre(self):
        return self.capacidad_max - len(self.espacio)
    
    def esta_lleno(self):
        if len(self.espacio) == self.capacidad_max:
            return True
        else:
            return False
        
    #Este metodo se llama cuando el vehiculo entra al taller
    def ingreso_vehiculo(self,vehiculo):
        if not self.esta_lleno:
            self.espacio.append(vehiculo)
            return True
        else:
            return False
    
    #Este metodo se llama cuando el vehiculo Entra a repararse
    def mandar_auto_a_reparacion(self):
        pass
    
    #Este metodo se llama cuando el vehiculo sale del taller
    def salida_vehiculo(self,vehiculo):
        self.espacio.remove(vehiculo)
        return True