from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from vistas_py.graficos import UiGraficos
import os

class ControladorGraficos(QDialog):
    def __init__(self):
        super(ControladorGraficos, self).__init__()
        self.pantalla_graficos = UiGraficos()
        self.pantalla_graficos.setupUi(self)
        self.cantidad_elevadores = 0
        self.cantidad_mecanicos = 0
        self.dias_simulacion = 0
        
        

    def comenzar_simulacion(self):
        try:
            self.cantidad_elevadores = int(self.menu_principal.cantidad_elevadores_input.text())
            self.cantidad_mecanicos = int(self.menu_principal.cantidad_mecanicos_input.text())
            self.dias_simulacion = int(self.menu_principal.dias_simulacion_input.text())
            self.done(0)
        except ValueError:
            self.menu_principal.mensaje_bienvenida_label.setText("Por Favor Complete todos los campos con valores numericos.")