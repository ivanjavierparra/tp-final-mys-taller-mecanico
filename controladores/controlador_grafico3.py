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

