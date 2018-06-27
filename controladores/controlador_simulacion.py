from PyQt5.QtWidgets import QMainWindow
from vistas_py.simulacion import Simulacion
from .controlador_grafico1 import ControladorGrafico1
from .controlador_grafico2 import ControladorGrafico2
from .controlador_grafico3 import ControladorGrafico3

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
        self.pantalla_simulacion.cant_elevadores_val_label.setText(str(self.cantidad_mecanicos))
        self.pantalla_simulacion.cant_mecanicos_val_label.setText(str(self.cantidad_mecanicos))
        self.pantalla_simulacion.dias_simulacion_val_label.setText(str(self.dias_simulacion))
        self.pantalla_simulacion.ver_grafico_uno_button.setEnabled(False)
        self.pantalla_simulacion.ver_grafico_dos_button.setEnabled(False)
        self.pantalla_simulacion.ver_grafico_tres_button.setEnabled(False)
        self.pantalla_simulacion.ver_grafico_uno_button.clicked.connect(self.mostrar_grafico_uno)
        self.pantalla_simulacion.ver_grafico_dos_button.clicked.connect(self.mostrar_grafico_dos)
        self.pantalla_simulacion.ver_grafico_tres_button.clicked.connect(self.mostrar_grafico_tres)
        
    def mostrar_grafico_uno(self):
        controlador_grafico_uno = ControladorGrafico1(self.elevadores, self.mecanicos, self.dias_simulacion)
        controlador_grafico_uno.exec_()

    def mostrar_grafico_dos(self):
        controlador_grafico_dos = ControladorGrafico2(self.elevadores, self.mecanicos, self.dias_simulacion)
        controlador_grafico_dos.exec_()
    
    def mostrar_grafico_tres(self):
        controlador_grafico_tres = ControladorGrafico3(self.elevadores, self.mecanicos, self.dias_simulacion)
        controlador_grafico_tres.exec_()

    def set_elevadores(self,arreglo):
        self.elevadores = arreglo
    
    def set_mecanicos(self,arreglo):
        self.mecanicos = arreglo