from PyQt5.QtWidgets import QMainWindow
from vistas_py.simulacion import Simulacion
from .controlador_graficos import ControladorGraficos

class ControladorSimulacion(QMainWindow):

    def __init__(self, cantidad_elevadores, cantidad_mecanicos, dias_simulacion):
        super(ControladorSimulacion, self).__init__()
        #Definicion de variables utilizadas parala simulación
        self.cantidad_elevadores = cantidad_elevadores
        self.cantidad_mecanicos = cantidad_mecanicos
        self.dias_simulacion = dias_simulacion

        #Cargamos la interfaz
        self.pantalla_simulacion = Simulacion()
        self.pantalla_simulacion.setupUi(self)

        #Confiración previa de atributos de entrada
        self.pantalla_simulacion.cant_elevadores_val_label.setText(str(self.cantidad_mecanicos))
        self.pantalla_simulacion.cant_mecanicos_val_label.setText(str(self.cantidad_mecanicos))
        self.pantalla_simulacion.dias_simulacion_val_label.setText(str(self.dias_simulacion))
        self.pantalla_simulacion.ver_informe_button.setEnabled(False)
        self.pantalla_simulacion.ver_informe_button.clicked.connect(self.mostrar_graficos)
        
    def mostrar_graficos(self):
        ventana = ControladorGraficos()
        ventana.exec_()

        