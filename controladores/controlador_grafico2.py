from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from vistas_py.grafico2 import UiGrafico2
import os
#Importamos las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from numpy.random import rand
from numpy import arange

class ControladorGrafico2(QDialog):
    def __init__(self, elevadores, mecanicos, dias):
        super(ControladorGrafico2, self).__init__()
        self.pantalla_graficos = UiGrafico2()
        self.pantalla_graficos.setupUi(self)
        self.cantidad_elevadores = 0
        self.cantidad_mecanicos = 0
        self.dias_simulacion = dias
        self.elevadores = elevadores
        self.mecanicos = mecanicos
        self.mostrarGraficoDos()




    def mostrarGraficoDos(self):
        ############ GRÁFICO 2 - Opción 2 ############

        #Estos son los valores por dia de cada elevador
        #elevador_1 = [600,400,500,300,300,400,500,543,223,123,231,233,344,444,233]
        #elevador_2 = [300,340,250,310,333,555,444,333,111,222,333,444,555,444,333]
        #elevador_3 = [210,234,345,354,354,354,333,555,444,222,111,222,111,222,111]
        #elevadores = []

        DIAS = self.dias_simulacion
        MINUTOS_DIAS = 600
        elevadores = []

        for i in range(DIAS):
            valor_promedio = 0
            for j in range(0,len(self.elevadores)):
                elevador_arreglo = self.elevadores[j].get_arreglo_horas_dia()#elijo elevador
                valor_promedio += elevador_arreglo[i]#en el dia


            valor_promedio = ((((valor_promedio)/len(self.elevadores))*100)/MINUTOS_DIAS)
            valor_promedio = float("{0:.2f}".format(valor_promedio))
            elevadores.append(valor_promedio)

    


        #Seteo los datos y el numero de dias
        dataset = elevadores
        date = np.arange(DIAS)

        labels = []
        for i in range(DIAS):
            j = i + 1
            labels.append("Día {0}".format(j))
        

        # variables para el grafico
        objects = labels
        y_pos = date
        performance = dataset
        
        # Con estas 2 lineas hago que el eje x tenga valor en porcentajes. Tambien establezco el tamaño del grafico. 
        fig,ax = plt.subplots(figsize=(15,5))#(ancho,alto)
        ax.xaxis.set_major_formatter(PercentFormatter(xmax=100))


        # aca creo el grafico
        plt.barh(y_pos, performance, align='center', alpha=0.5)
        plt.yticks(y_pos, objects)
        plt.xlabel('Porcentaje de Uso')
        plt.title('Porcentaje de Uso de Elevadores')
 
    
        # esto le pone a cada barra el valor que posee
        for a,b in zip(dataset,date):
            plt.text(a, b, str(a) + " %",verticalalignment='center',horizontalalignment='left')


        plt.savefig('grafico2.png')
        pixmap = QPixmap("grafico2.png")
        pixmap = pixmap.scaled(1000, 500)
        self.pantalla_graficos.grafico_label.setPixmap(pixmap)