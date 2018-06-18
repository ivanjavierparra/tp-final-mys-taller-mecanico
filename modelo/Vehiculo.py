class Vehiculo:
    """
    Clase que representa el vehiculo
    """
    def __init__(self, patente, usa_elevador=False, espera=None, =None, tiempo_total):
        self.patente = patente
        self.usa_elevador = usa_elevador
        self.tiempo_espera = espera
        self.tiempo_reparacion = reparacion
        self.tiempo_total = tiempo_total
        self.reparado = False