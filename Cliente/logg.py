# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Loggin(object):
    def setupUi(self, Loggin):
        Loggin.setObjectName(_fromUtf8("Loggin"))
        Loggin.resize(415, 310)
        self.centralwidget = QtGui.QWidget(Loggin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 60, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 91, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 57, 181, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 100, 181, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 160, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 160, 99, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 230, 99, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        
        self.menubar = QtGui.QMenuBar(Loggin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.statusbar = QtGui.QStatusBar(Loggin)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        

        self.retranslateUi(Loggin)
        QtCore.QMetaObject.connectSlotsByName(Loggin)
      

    def retranslateUi(self, Loggin):
        Loggin.setWindowTitle(_translate("Loggin", "Loggin", None))
        self.label.setText(_translate("Loggin", "Usuario:", None))
        self.label_2.setText(_translate("Loggin", "Contraseña:", None))
        self.pushButton.setText(_translate("Loggin", "Cancelar", None))
        self.pushButton_2.setText(_translate("Loggin", "Entrar", None))
        self.pushButton_3.setText(_translate("Loggin", "Registrarse", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Loggin = QtGui.QMainWindow()
    ui = Ui_Loggin()
    ui.setupUi(Loggin)
    Loggin.show()
    sys.exit(app.exec_())

