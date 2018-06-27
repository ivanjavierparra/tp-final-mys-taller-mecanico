from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from vistas_py.grafico1 import UiGrafico1
import os
#Importamos las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from numpy.random import rand
from numpy import arange

class ControladorGrafico1(QDialog):
    def __init__(self, elevadores, mecanicos, dias):
        super(ControladorGrafico1, self).__init__()
        self.pantalla_graficos = UiGrafico1()
        self.pantalla_graficos.setupUi(self)
        self.cantidad_elevadores = 0
        self.cantidad_mecanicos = 0
        self.dias_simulacion = dias
        self.elevadores = elevadores
        self.mecanicos = mecanicos
        self.mostrarGraficoUno()

    #en main esta la llamada a controladorSimulacion, que recibe los mecanicos y elevadores
    #dsadkldnsalksjdajdlksajdlaksjdlksajdldjsk
    def mostrarGraficoUno(self):
        # create data
        print("putasooo")
        print("Elevadores: " + str(self.elevadores)) 
        print("Mecanicos: " + str(self.mecanicos))
        print("Dias de Simulacion: " + str(self.dias_simulacion))
        print("tamaño: " + str(len(self.elevadores)))
        #Estas son las listas de cada elevador. Cada lugar del arreglo representa un dia.
        
        elevadores = np.arange(len(self.elevadores))
        print(str(self.elevadores[0].get_arreglo_horas_dia()))
        print(str(self.elevadores[1].get_arreglo_horas_dia()))
        print(str(self.elevadores[2].get_arreglo_horas_dia()))##### el problema es que tengo que agarra el arreglo!!!!PELOTUDO!!!
        
        #valor_1 = float("{0:.2f}".format(((np.mean(elevador_2)*100)/DIA)))
        #valor_2 = float("{0:.2f}".format(((np.mean(elevador_2)*100)/DIA)))
        #valor_3 = float("{0:.2f}".format(((np.mean(elevador_3)*100)/DIA)))
        
        dataset = [0] * len(self.elevadores)
        for i in range(0,len(self.elevadores)):
            elevador_arreglo = self.elevadores[i].get_arreglo_horas_dia()
            dataset[i]  = float("{0:.2f}".format(((np.mean(elevador_arreglo)*100)/self.dias_simulacion)))
            


        #arreglo con los promedios de todos los dias.
        #dataset = [valor_1,valor_2,valor_3]


        # esto es para poner en el eje y porcentajes. 
        #formatter = PercentFormatter(xmax=600)
        fig,ax = plt.subplots(figsize=(7,7))
        #ax.yaxis.set_major_formatter(formatter)
        ax.yaxis.set_major_formatter(PercentFormatter(xmax=100))

        # esto le pone a cada bar el valor que posee
        for a,b in zip(elevadores, dataset):
            plt.text(a, b, str(b) + " %",verticalalignment='top',horizontalalignment='center')
        

        # seteo los datos    
        plt.bar(elevadores,dataset, color='#FFC222',width=0.30, alpha=0.5)

        labels = []
        for i in range(0,len(self.elevadores)):
            j = i + 1
            labels.append("Elevador " + str(j))
        
        plt.xticks(elevadores,labels)

        # titulos
        plt.title("Porcentaje de Uso de los Elevadores")
        plt.xlabel("Elevadores")
        plt.ylabel("Porcentaje de Uso")

        plt.savefig('fig1.png')

        self.pantalla_graficos.grafico_label.setPixmap(QPixmap("fig1.png"))

        



    



    