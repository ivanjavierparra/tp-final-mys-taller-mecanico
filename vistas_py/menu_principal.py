# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_principal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MenuPrincipal(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(548, 347)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 531, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comenzar_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.comenzar_button.setObjectName("comenzar_button")
        self.gridLayout.addWidget(self.comenzar_button, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cantidad_elevadores_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.cantidad_elevadores_input.setObjectName("cantidad_elevadores_input")
        self.gridLayout_2.addWidget(self.cantidad_elevadores_input, 3, 1, 1, 1)
        self.cantidad_mecanicos_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.cantidad_mecanicos_label.setObjectName("cantidad_mecanicos_label")
        self.gridLayout_2.addWidget(self.cantidad_mecanicos_label, 1, 0, 1, 1)
        self.cantidad_mecanicos_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.cantidad_mecanicos_input.setObjectName("cantidad_mecanicos_input")
        self.gridLayout_2.addWidget(self.cantidad_mecanicos_input, 1, 1, 1, 1)
        self.dias_simulacion_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dias_simulacion_label.setObjectName("dias_simulacion_label")
        self.gridLayout_2.addWidget(self.dias_simulacion_label, 0, 0, 1, 1)
        self.cantidad_elevadores_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.cantidad_elevadores_label.setObjectName("cantidad_elevadores_label")
        self.gridLayout_2.addWidget(self.cantidad_elevadores_label, 3, 0, 1, 1)
        self.dias_simulacion_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.dias_simulacion_input.setObjectName("dias_simulacion_input")
        self.gridLayout_2.addWidget(self.dias_simulacion_input, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.mensaje_bienvenida_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.mensaje_bienvenida_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mensaje_bienvenida_label.setObjectName("mensaje_bienvenida_label")
        self.gridLayout.addWidget(self.mensaje_bienvenida_label, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Menú Principal - Simulación de un Taller Mecánico"))
        Dialog.setWindowIcon(QtGui.QIcon('car.png'))
        self.comenzar_button.setText(_translate("Dialog", "Comenzar la Simulación"))
        self.cantidad_mecanicos_label.setText(_translate("Dialog", "Cantidad de Mecánicos"))
        self.dias_simulacion_label.setText(_translate("Dialog", "Dias de Simulación"))
        self.cantidad_elevadores_label.setText(_translate("Dialog", "Cantidad de Elevadores"))
        self.mensaje_bienvenida_label.setText(_translate("Dialog", "Bienvenido al sistema de Simulación del Taller Mecanico\n"
"Ingrese por favor los valores de la simulación:"))

