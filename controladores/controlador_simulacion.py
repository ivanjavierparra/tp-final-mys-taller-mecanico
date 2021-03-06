from PyQt5.QtWidgets import QMainWindow
from vistas_py.simulacion import Simulacion
import os
#Importamos las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from numpy.random import rand
from numpy import arange

class ControladorSimulacion(QMainWindow):

    def __init__(self, cantidad_elevadores, cantidad_mecanicos, dias_simulacion, elevadores=None, mecanicos=None):
        super(ControladorSimulacion, self).__init__()
        #Definicion de variables utilizadas parala simulación
        self.cantidad_elevadores = cantidad_elevadores
        self.cantidad_mecanicos = cantidad_mecanicos
        self.dias_simulacion = dias_simulacion
        self.elevadores = elevadores
        self.mecanicos = mecanicos

        #Cargamos la interfaz
        self.pantalla_simulacion = Simulacion()
        self.pantalla_simulacion.setupUi(self)

        #Confiración previa de atributos de entrada
        self.pantalla_simulacion.cant_elevadores_val_label.setText(str(self.cantidad_elevadores))
        self.pantalla_simulacion.cant_mecanicos_val_label.setText(str(self.cantidad_mecanicos))
        self.pantalla_simulacion.dias_simulacion_val_label.setText(str(self.dias_simulacion))
        self.pantalla_simulacion.ver_grafico_uno_button.setEnabled(False)
        self.pantalla_simulacion.ver_grafico_dos_button.setEnabled(False)
        self.pantalla_simulacion.ver_grafico_tres_button.setEnabled(False)
        self.pantalla_simulacion.ver_grafico_uno_button.clicked.connect(self.mostrar_grafico_uno)
        self.pantalla_simulacion.ver_grafico_dos_button.clicked.connect(self.mostrar_grafico_dos)
        self.pantalla_simulacion.ver_grafico_tres_button.clicked.connect(self.mostrar_grafico_tres)
        
    def mostrar_grafico_uno(self):
        cantidad_elevadores = 0
        cantidad_mecanicos = 0

        elevadores = np.arange(len(self.elevadores))
        
        #valor_1 = float("{0:.2f}".format(((np.mean(elevador_2)*100)/DIA)))
        #valor_2 = float("{0:.2f}".format(((np.mean(elevador_2)*100)/DIA)))
        #valor_3 = float("{0:.2f}".format(((np.mean(elevador_3)*100)/DIA)))
        
        dataset = [0] * len(self.elevadores)
        for i in range(0,len(self.elevadores)):
            elevador_arreglo = self.elevadores[i].get_arreglo_horas_dia()
            dataset[i]  = float("{0:.2f}".format(((np.mean(elevador_arreglo)*100)/(600))))
            
            


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
        plt.title("Porcentaje de Uso de c/Elevadores en " + str(self.dias_simulacion) + " días")
        plt.xlabel("Elevadores")
        plt.ylabel("Porcentaje de Uso")
        plt.show()

    def mostrar_grafico_dos(self):
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
        plt.title('Porcentaje de Uso de los '+  str(len(self.elevadores))   + ' Elevadores por día (En ' + str(self.dias_simulacion) + ' días)')
 
    
        # esto le pone a cada barra el valor que posee
        for a,b in zip(dataset,date):
            plt.text(a, b, str(a) + " %",verticalalignment='center',horizontalalignment='left')
        plt.show()
    
    def mostrar_grafico_tres(self):
        plt.clf()
        lista = []
        
        for j in range(0,len(self.elevadores)):
            elevador_arreglo = self.elevadores[j].get_arreglo_horas_dia()
            lista.append(elevador_arreglo)
        
        promedio_uso_elevadores = np.mean(lista)
        #calculo porcentajes
        total = 600 # horas por dia
        proportion_ocupado = (promedio_uso_elevadores * 100)/600
        proportion_desocupado = 100 - proportion_ocupado
        
        valor1 = float("{0:.2f}".format(proportion_desocupado))
        valor2 = float("{0:.2f}".format(proportion_ocupado))

        #Por cada mecanico creo su barra
        plt.bar('Elevadores', proportion_desocupado, width=0.5, label='Desocupado: ' + str(valor1) + "%", color='gold', bottom=proportion_ocupado)
        plt.bar('Elevadores', proportion_ocupado, width=0.5, label='Ocupado: ' + str(valor2) + "%", color='#CD853F')

        plt.legend(loc="best")

        #Seteo atributos del grafico
        plt.ylabel("Porcentaje de Ocupación")
        plt.xlabel("Elevadores")

        plt.title("Porcentaje de Uso de los "+ str(len(self.elevadores)) + " Elevadores en promedio por día durante " + str(self.dias_simulacion) + " días")
        plt.ylim=1.0

        plt.setp(plt.gca().get_xticklabels(), horizontalalignment='center')

        plt.show()

    def set_elevadores(self,arreglo):
        self.elevadores = arreglo
    
    def set_mecanicos(self,arreglo):
        self.mecanicos = arreglo