class Elevador:
    """
    Clase que representa el elevador
    """
    def __init__(self,dias_elevador):
        self.disponible = True
        self.tiempo_uso = 0
        self.dias_elevador = dias_elevador
        self.arreglo_horas_dia = [0] * self.dias_elevador

    def get_disponible(self):
        return self.disponible
    
    def set_disponible(self, nuevo_valor):
        self.disponible = nuevo_valor
        
    def get_tiempo_uso(self):
        return self.tiempo_uso
    
    def set_tiempo_uso(self, nuevo_valor):
        self.tiempo_uso = nuevo_valor

    def get_arreglo_horas_dia(self):
        return self.arreglo_horas_dia
    
    def set_valor_arreglo(self,dia,valor):
        self.arreglo_horas_dia[dia] += valor
    
    def get_valor_arreglo(self,dia):
        return self.arreglo_horas_dia[dia]
    #NOTA 1: elevador tendría que tener lista[dias] donde guarda por c/dia el tiempo de uso.
    #NOTA 2: funcion getDia(valor_del_reloj)---> dia = (valor_del_reloj/600) + 1   ---> hay que truncar... 