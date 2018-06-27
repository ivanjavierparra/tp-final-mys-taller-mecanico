class Vehiculo:
    """
    Clase que representa el vehiculo
    """
    def __init__(self, patente, usa_elevador=False, espera=None, reparacion=None, tiempo_total=0,tiempo_llegada=0):
        self.patente = patente
        self.usa_elevador = usa_elevador
        self.tiempo_espera = espera #desde que llega al taller hasta que comienza la reparacion
        self.tiempo_reparacion = reparacion # lo tarda en repararce 
        self.tiempo_total = tiempo_total    # lo que va a estar en el taller
        self.tiempo_llegada = tiempo_llegada
        self.reparado = False

    def __str__(self):
        if self.usa_elevador:
            elevador = "Usa Elevador"
        else:
            elevador = "No usa Elevador"
        return "{0}-Tiempo Reparacion:{1}-Tiempo Permanencia:{2}".format(elevador,self.tiempo_reparacion,self.tiempo_total)

    def get_usa_elevador(self):
        return self.usa_elevador

    def get_tiempo_espera(self):
        return self.tiempo_espera

    def get_tiempo_llegada(self):
        return self.tiempo_llegada

    def get_tiempo_reparacion(self):
        return self.tiempo_reparacion

    def get_tiempo_total(self):
        return self.tiempo_total

    def get_reparado(self):
        return self.reparado

    def set_tiempo_espera(self, un_tiempo):
        self.tiempo_espera = un_tiempo

    def set_tiempo_llegada(self, un_tiempo):
        self.tiempo_llegada = un_tiempo

    def set_tiempo_reparacion(self, un_tiempo_reparacion):
        self.tiempo_reparacion = un_tiempo_reparacion

    def set_reparado(self, un_booleano):
        self.reparado = un_booleano