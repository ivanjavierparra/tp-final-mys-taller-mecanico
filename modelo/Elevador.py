class Elevador:
    """
    Clase que representa el elevador
    """
    def __init__(self):
        self.disponible = True
        self.tiempo_uso = 0
        
    def get_disponible(self):
        return self.disponible
    
    def set_disponible(self, nuevo_valor):
        self.disponible = nuevo_valor
        
    def get_tiempo_uso(self):
        return self.tiempo_uso
    
    def set_tiempo_uso(self, nuevo_valor):
        self.tiempo_uso = nuevo_valor

    #NOTA 1: elevador tendría que tener lista[dias] donde guarda por c/dia el tiempo de uso.
    #NOTA 2: funcion getDia(valor_del_reloj)---> dia = (valor_del_reloj/600) + 1   ---> hay que truncar... 