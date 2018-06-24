from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from vistas_py.menu_principal import MenuPrincipal
from .controlador_simulacion import ControladorSimulacion
import os

class ControladorMenuPrincipal(QMainWindow):
    def __init__(self):
        super(ControladorMenuPrincipal, self).__init__()
        self.menu_principal = MenuPrincipal()
        self.menu_principal.setupUi(self)
        self.menu_principal.comenzar_button.clicked.connect(self.comenzar_simulacion)

    def comenzar_simulacion(self):
        try:
            cantidad_elevadores = int(self.menu_principal.cantidad_elevadores_input.text())
            cantidad_mecanicos = int(self.menu_principal.cantidad_mecanicos_input.text())
            dias_simulacion = int(self.menu_principal.dias_simulacion_input.text())
            ventana = ControladorSimulacion(cantidad_elevadores,cantidad_mecanicos,dias_simulacion)
            ventana.exec_()
        except ValueError:
            self.menu_principal.mensaje_bienvenida_label.setText("Por Favor Complete todos los campos con valores numericos.")