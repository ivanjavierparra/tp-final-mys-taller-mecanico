# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grafico3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UiGrafico3(object):
    def setupUi(self, Grafico3):
        Grafico3.setObjectName("Grafico3")
        Grafico3.resize(1020, 520)
        self.grafico_label = QtWidgets.QLabel(Grafico3)
        self.grafico_label.setGeometry(QtCore.QRect(10, 10, 1000, 500))
        self.grafico_label.setAlignment(QtCore.Qt.AlignCenter)
        self.grafico_label.setObjectName("grafico_label")

        self.retranslateUi(Grafico3)
        QtCore.QMetaObject.connectSlotsByName(Grafico3)

    def retranslateUi(self, Grafico3):
        _translate = QtCore.QCoreApplication.translate
        Grafico3.setWindowTitle(_translate("Grafico3", "Graficos - Simulación de un Taller Mecánico"))
        self.grafico_label.setText(_translate("Grafico3", "grafico"))

