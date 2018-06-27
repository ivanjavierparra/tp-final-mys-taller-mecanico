class Reloj:
    """
    Clase que representa un reloj
    """
    def __init__(self):
        self.valor = 0 #en minutos
        
    def get_valor(self):
        return self.valor
    
    def set_valor(self, nuevo_valor):
        self.valor = nuevo_valor

    def adelantar(self, nuevo_valor):
        self.valor += nuevo_valor
        