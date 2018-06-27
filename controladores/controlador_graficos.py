from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from vistas_py.graficos import UiGraficos
import os
#Importamos las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from numpy.random import rand
from numpy import arange

class ControladorGraficos(QDialog):
    def __init__(self, elevadores, mecanicos, dias):
        super(ControladorGraficos, self).__init__()
        self.pantalla_graficos = UiGraficos()
        self.pantalla_graficos.setupUi(self)
        self.cantidad_elevadores = 0
        self.cantidad_mecanicos = 0
        self.dias_simulacion = dias
        self.elevadores = elevadores
        self.mecanicos = mecanicos
        self.mostrarGraficoUno()
        self.mostrarGraficoDos()
        self.mostrarGraficoTres()

    def comenzar_simulacion(self):
        try:
            self.cantidad_elevadores = int(self.menu_principal.cantidad_elevadores_input.text())
            self.cantidad_mecanicos = int(self.menu_principal.cantidad_mecanicos_input.text())
            self.dias_simulacion = int(self.menu_principal.dias_simulacion_input.text())
            self.done(0)
        except ValueError:
            self.menu_principal.mensaje_bienvenida_label.setText("Por Favor Complete todos los campos con valores numericos.")
    
    
    
    


    #en main esta la llamada a controladorSimulacion, que recibe los mecanicos y elevadores
    #dsadkldnsalksjdajdlksajdlaksjdlksajdldjsk
    def mostrarGraficoUno(self):
        # create data
        print("putasooo")
        print("Elevadores: " + str(self.elevadores)) 
        print("Mecanicos: " + str(self.mecanicos))
        print("Dias de Simulacion: " + str(self.dias_simulacion))
        
        #Estas son las listas de cada elevador. Cada lugar del arreglo representa un dia.
        elevador_1 = [600,400,500]
        elevador_2 = [300,340,250]
        elevador_3 = [210,234,345]

        DIA = 600 #minutos maximos que puede usarse un elevador

        elevadores = np.arange(3)

        valor_1 = float("{0:.2f}".format(((np.mean(elevador_2)*100)/DIA)))
        valor_2 = float("{0:.2f}".format(((np.mean(elevador_2)*100)/DIA)))
        valor_3 = float("{0:.2f}".format(((np.mean(elevador_3)*100)/DIA)))

        #arreglo con los promedios de todos los dias.
        dataset = [valor_1,valor_2,valor_3]


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
        plt.xticks(elevadores,('Elevador 1','Elevador 2','Elevador 3'))

        # titulos
        plt.title("Porcentaje de Uso de los Elevadores")
        plt.xlabel("Elevadores")
        plt.ylabel("Porcentaje de Uso")



        plt.savefig('fig1.png')

        self.pantalla_graficos.grafico_uno_label.setPixmap(QPixmap("fig1.png"))

        



    def mostrarGraficoDos(self):
        ############ GRÁFICO 2 - Opción 2 ############

        #Estos son los valores por dia de cada elevador
        elevador_1 = [600,400,500,300,300,400,500,543,223,123,231,233,344,444,233]
        elevador_2 = [300,340,250,310,333,555,444,333,111,222,333,444,555,444,333]
        elevador_3 = [210,234,345,354,354,354,333,555,444,222,111,222,111,222,111]
        elevadores = []

        DIAS = 15
        MINUTOS_DIAS = 600
        for i in range(DIAS):
            valor_promedio = ((((elevador_1[i] + elevador_2[i] + elevador_3[i])/3)*100)/MINUTOS_DIAS)
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


        plt.savefig('fig2.png')

        self.pantalla_graficos.grafico_dos_label.setPixmap(QPixmap("fig2.png"))



    def mostrarGraficoTres(self):
        #Por cada mecanico tengo dos arreglos: uno de ocupado y otro de desocupado.
        plt.clf()
        ocupado = np.array([38, 17, 26, 19, 15])
        desocupado = np.array([62, 83, 74, 81, 85])

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

        self.pantalla_graficos.grafico_tres_label.setPixmap(QPixmap("fig3.png"))