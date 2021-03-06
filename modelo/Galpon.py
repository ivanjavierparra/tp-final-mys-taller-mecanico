class Galpon:
    """
    Clase que representa el Galpon
    """
    def __init__(self, capacidad):
        self.capacidad_max = capacidad
        self.espacio = []
        
    def get_espacio_libre(self):
        return self.capacidad_max - len(self.espacio)
    
    def get_espacio_ocupado(self):
        return len(self.espacio)
    
    def esta_lleno(self):
        return len(self.espacio) == self.capacidad_max
        
    #Este metodo se llama cuando el vehiculo entra al taller
    def ingreso_vehiculo(self,vehiculo):
        if not self.esta_lleno():
            self.espacio.append(vehiculo)
            return True
        else:
            return False
    
    def get_proximos_vehiculos(self):
        vehiculos_no_reparados = []
        for vehiculo in self.espacio:
            if not vehiculo.reparado: 
                vehiculos_no_reparados.append(vehiculo)
        return vehiculos_no_reparados

    #Este metodo se llama cuando el vehiculo sale del taller
    def salida_vehiculo(self,vehiculo):
        self.espacio.remove(vehiculo)
        return True