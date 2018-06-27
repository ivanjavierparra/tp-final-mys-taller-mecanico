from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from vistas_py.grafico3 import UiGrafico3
import os
#Importamos las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from numpy.random import rand
from numpy import arange

class ControladorGrafico3(QDialog):
    def __init__(self, elevadores, mecanicos, dias):
        super(ControladorGrafico3, self).__init__()
        self.pantalla_graficos = UiGrafico3()
        self.pantalla_graficos.setupUi(self)
        self.cantidad_elevadores = 0
        self.cantidad_mecanicos = 0
        self.dias_simulacion = dias
        self.elevadores = elevadores
        self.mecanicos = mecanicos
        self.mostrarGraficoTres()


    def mostrarGraficoTres(self):
        #Por cada mecanico tengo dos arreglos: uno de ocupado y otro de desocupado.
        plt.clf()
        ocupado = np.array([38, 17, 26, 19, 15])
        desocupado = np.array([62, 83, 74, 81, 85])

        for mecanico in self.mecanicos:
            print(str(mecanico.get_tiempo_uso_dia()))

        """
        for mecanico in self.mecanicos:
            print(str(mecanico.get_tiempo_uso_dia()))
            
        #calculo porcentajes
        total = ocupado + desocupado
        proportion_ocupado = np.true_divide(ocupado, total) * 100
        proportion_desocupado = np.true_divide(desocupado, total) * 100

        #Por cada mecanico creo su barra
        plt.bar('Mecánico 1', proportion_ocupado, width=0.5, label='Ocupado', color='gold', bottom=proportion_desocupado)
        plt.bar('Mecánico 1', proportion_desocupado, width=0.5, label='Desocupado', color='#CD853F')

        plt.legend(loc="best")
        #legend toma los valores de "label" en "plt.bar"
        #opciones de legend en: https://matplotlib.org/api/legend_api.html

        plt.bar('Mecánico 2', 50, width=0.5, label='golds', color='gold', bottom=50)
        plt.bar('Mecánico 2', 50, width=0.5, label='bronzes', color='#CD853F')

        plt.bar('Mecánico 3', proportion_ocupado, width=0.5, label='golds', color='gold', bottom=proportion_desocupado)
        plt.bar('Mecánico 3', proportion_desocupado, width=0.5, label='bronzes', color='#CD853F')

        #Seteo atributos del grafico
        plt.ylabel("Porcentaje de Ocupación")
        plt.xlabel("Mecánicos")

        plt.title("Porcentaje de Ocupacación de los Mecánicos")
        plt.ylim=1.0

        # rotate axis labels
        plt.setp(plt.gca().get_xticklabels(), horizontalalignment='center')
        #plt.savefig('fig1.png')

        plt.savefig('fig3.png')
        pixmap = QPixmap("fig3.png")
        pixmap = pixmap.scaled(1000, 500)
        self.pantalla_graficos.grafico_label.setPixmap(pixmap)
        """