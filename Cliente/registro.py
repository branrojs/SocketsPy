# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registro.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(781, 535)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 40, 61, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 90, 68, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 140, 68, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 190, 68, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 240, 111, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 290, 41, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 340, 101, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 390, 91, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(70, 440, 141, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 30, 261, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 80, 261, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(230, 130, 261, 31))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_4 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(230, 180, 261, 31))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.textEdit_5 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(230, 230, 261, 31))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.textEdit_6 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(230, 280, 261, 31))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.textEdit_7 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(230, 330, 261, 31))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.textEdit_8 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(230, 380, 261, 31))
        self.textEdit_8.setObjectName(_fromUtf8("textEdit_8"))
        self.textEdit_9 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(230, 430, 261, 31))
        self.textEdit_9.setObjectName(_fromUtf8("textEdit_9"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 170, 151, 61))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 260, 151, 61))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Registrar Usuarios", None))
        self.label.setText(_translate("MainWindow", "Cédula:", None))
        self.label_2.setText(_translate("MainWindow", "Nombre:", None))
        self.label_3.setText(_translate("MainWindow", "Apellido:", None))
        self.label_4.setText(_translate("MainWindow", "Correo:", None))
        self.label_5.setText(_translate("MainWindow", "              Telefono:", None))
        self.label_6.setText(_translate("MainWindow", "País:", None))
        self.label_7.setText(_translate("MainWindow", "Código Postal:", None))
        self.label_8.setText(_translate("MainWindow", "Contraseña:", None))
        self.label_9.setText(_translate("MainWindow", "Repetir Contraseña:", None))
        self.pushButton.setText(_translate("MainWindow", "REGISTRAR", None))
        self.pushButton_2.setText(_translate("MainWindow", "CANCELAR", None))

   


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

