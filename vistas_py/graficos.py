# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graficos.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UiGraficos(object):
    def setupUi(self, Graficos):
        Graficos.setObjectName("Graficos")
        Graficos.resize(764, 486)
        self.gridLayoutWidget = QtWidgets.QWidget(Graficos)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 751, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.contenedor_grafico_uno = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.contenedor_grafico_uno.setObjectName("contenedor_grafico_uno")
        self.grafico_uno_label = QtWidgets.QLabel(self.contenedor_grafico_uno)
        self.grafico_uno_label.setGeometry(QtCore.QRect(1, 29, 371, 201))
        self.grafico_uno_label.setObjectName("grafico_uno_label")
        self.gridLayout.addWidget(self.contenedor_grafico_uno, 0, 0, 1, 1)
        self.contenedor_grafico_dos = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.contenedor_grafico_dos.setObjectName("contenedor_grafico_dos")
        self.grafico_dos_label = QtWidgets.QLabel(self.contenedor_grafico_dos)
        self.grafico_dos_label.setGeometry(QtCore.QRect(11, 29, 351, 201))
        self.grafico_dos_label.setObjectName("grafico_dos_label")
        self.gridLayout.addWidget(self.contenedor_grafico_dos, 0, 1, 1, 1)
        self.contenedor_grafico_tres = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.contenedor_grafico_tres.setObjectName("contenedor_grafico_tres")
        self.grafico_tres_label = QtWidgets.QLabel(self.contenedor_grafico_tres)
        self.grafico_tres_label.setGeometry(QtCore.QRect(1, 29, 371, 201))
        self.grafico_tres_label.setObjectName("grafico_tres_label")
        self.gridLayout.addWidget(self.contenedor_grafico_tres, 1, 0, 1, 1)
        self.contenedor_grafico_cuatro = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.contenedor_grafico_cuatro.setObjectName("contenedor_grafico_cuatro")
        self.grafico_cuatro_label = QtWidgets.QLabel(self.contenedor_grafico_cuatro)
        self.grafico_cuatro_label.setGeometry(QtCore.QRect(0, 30, 361, 191))
        self.grafico_cuatro_label.setObjectName("grafico_cuatro_label")
        self.gridLayout.addWidget(self.contenedor_grafico_cuatro, 1, 1, 1, 1)

        self.retranslateUi(Graficos)
        QtCore.QMetaObject.connectSlotsByName(Graficos)

    def retranslateUi(self, Graficos):
        _translate = QtCore.QCoreApplication.translate
        Graficos.setWindowTitle(_translate("Graficos", "Graficos"))
        self.contenedor_grafico_uno.setTitle(_translate("Graficos", "GroupBox1"))
        self.grafico_uno_label.setText(_translate("Graficos", "TextLabel"))
        self.contenedor_grafico_dos.setTitle(_translate("Graficos", "GroupBox2"))
        self.grafico_dos_label.setText(_translate("Graficos", "TextLabel"))
        self.contenedor_grafico_tres.setTitle(_translate("Graficos", "GroupBox3"))
        self.grafico_tres_label.setText(_translate("Graficos", "TextLabel"))
        self.contenedor_grafico_cuatro.setTitle(_translate("Graficos", "GroupBox4"))
        self.grafico_cuatro_label.setText(_translate("Graficos", "TextLabel"))

