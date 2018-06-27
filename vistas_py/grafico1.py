# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grafico1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UiGrafico1(object):
    def setupUi(self, Grafico1):
        Grafico1.setObjectName("Grafico1")
        Grafico1.resize(720, 720)
        self.grafico_label = QtWidgets.QLabel(Grafico1)
        self.grafico_label.setGeometry(QtCore.QRect(10, 10, 700, 700))
        self.grafico_label.setAlignment(QtCore.Qt.AlignCenter)
        self.grafico_label.setObjectName("grafico_label")

        self.retranslateUi(Grafico1)
        QtCore.QMetaObject.connectSlotsByName(Grafico1)

    def retranslateUi(self, Grafico1):
        _translate = QtCore.QCoreApplication.translate
        Grafico1.setWindowTitle(_translate("Grafico1", "Grafico"))
        self.grafico_label.setText(_translate("Grafico1", "grafico"))

