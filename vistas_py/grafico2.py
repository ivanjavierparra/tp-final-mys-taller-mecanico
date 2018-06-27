# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grafico2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UiGrafico2(object):
    def setupUi(self, Grafico2):
        Grafico2.setObjectName("Grafico2")
        Grafico2.resize(1020, 520)
        self.grafico_label = QtWidgets.QLabel(Grafico2)
        self.grafico_label.setGeometry(QtCore.QRect(10, 10, 1000, 500))
        self.grafico_label.setAlignment(QtCore.Qt.AlignCenter)
        self.grafico_label.setObjectName("grafico_label")

        self.retranslateUi(Grafico2)
        QtCore.QMetaObject.connectSlotsByName(Grafico2)

    def retranslateUi(self, Grafico2):
        _translate = QtCore.QCoreApplication.translate
        Grafico2.setWindowTitle(_translate("Grafico2", "Graficos - Simulación de un Taller Mecánico"))
        self.grafico_label.setText(_translate("Grafico2", "grafico"))

