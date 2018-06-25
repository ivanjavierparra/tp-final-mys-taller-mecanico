from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from vistas_py.menu_principal import MenuPrincipal
import os

class ControladorMenuPrincipal(QDialog):
    def __init__(self):
        super(ControladorMenuPrincipal, self).__init__()
        self.menu_principal = MenuPrincipal()
        self.menu_principal.setupUi(self)
        self.cantidad_elevadores = 0
        self.cantidad_mecanicos = 0
        self.dias_simulacion = 0
        self.menu_principal.comenzar_button.clicked.connect(self.comenzar_simulacion)
        

    def comenzar_simulacion(self):
        try:
            self.cantidad_elevadores = int(self.menu_principal.cantidad_elevadores_input.text())
            self.cantidad_mecanicos = int(self.menu_principal.cantidad_mecanicos_input.text())
            self.dias_simulacion = int(self.menu_principal.dias_simulacion_input.text())
            self.done(0)
        except ValueError:
            self.menu_principal.mensaje_bienvenida_label.setText("Por Favor Complete todos los campos con valores numericos.")