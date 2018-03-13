#importamos sys
import sys
#importamos QtGui, QtCore
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from logg import Ui_Loggin
from registro import Ui_MainWindow	
from zoket import client
from user import Ui_Uss
from CServidor import MainWindow
from CServidor import Ui_Dialog

import MySQLdb

class MainWindou(QtGui.QWidget):
	def __init__(self, parent = None):
		self.ui_ad= MainWindow()
		self.ui_ad.show()

class MyTableModela(QAbstractTableModel):
	def __init__(self, datain, parent=None, *args):
		QAbstractTableModel.__init__(self, parent, *args)
		self.arraydata = datain

	def rowCount(self, parent):
		return len(self.arraydata)

	def columnCount(self, parent):
		return len(self.arraydata[0])

	def data(self, index,role):
		if not index.isValid():
			return QVariant()
		elif role != Qt.DisplayRole:
			return QVariant()
		return QVariant(self.arraydata[index.row()][index.column()])
        

class Ussa(QtGui.QWidget):
	def __init__(self,ida, parent=None):
		super(Ussa, self).__init__(parent)
		global nom,tun 
		nom= ida
		self.ui_u = Ui_Uss()
		self.ui_u.setupUi(self)
		QtCore.QObject.connect(self.ui_u.Editar, QtCore.SIGNAL("clicked()"), self.editarus)
		QtCore.QObject.connect(self.ui_u.Eliminar_2, QtCore.SIGNAL("clicked()"), self.guardardatos)
		QtCore.QObject.connect(self.ui_u.Eliminar, QtCore.SIGNAL("clicked()"), self.elimicar)
		QtCore.QObject.connect(self.ui_u.buscar, QtCore.SIGNAL("clicked()"), self.mostrarcat)
		QtCore.QObject.connect(self.ui_u.Comprar, QtCore.SIGNAL("clicked()"), self.comprar)

		con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
		cursor = con.cursor()
		cursor.execute("SELECT idCarrito, Nombre, Descripcion, cant FROM Carrito, Usuarios, Articulos Where Uid=idUsuarios and Aid=idArticulos and Nombre= '%s';"%(ida))
		save = cursor.fetchall()
		table = MyTableModela(save, self)
		self.ui_u.carritotable.setModel(table)
		cursor.execute("SELECT idFacturacion as '#Factura', Fecha, Descripcion as 'Articulo Vendido', PrecioU as 'Precio Unitario', Nombre as 'Comprador', idUsuarios as 'id' FROM Facturacion,Articulos_Vendidos, Articulos, Usuarios where Cod_Factura=idFacturacion AND cod_articulo = idArticulos AND User_id = idUsuarios and Nombre ='%s';"%(ida))
		sort = cursor.fetchall()
		table2 = MyTableModela(sort, self)
		self.ui_u.artobtable.setModel(table2)
		cursor.close()
		con.close()

	def editarus(self):
		con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
		cursor = con.cursor()
		cursor.execute("SELECT idUsuarios, Nombre, Correo, Descrip as 'Pais', Telefono, Cod_pais FROM Usuarios, Pais where Cod_pais=idPais and Nombre = '%s'"%(nom))
		save = cursor.fetchall()
		cursor.close()
		con.close()
		self.ui_u.lineEdit_5.setText(str(save[0][0]))
		self.ui_u.lineEdit_4.setText(str(save[0][1]))
		self.ui_u.lineEdit_3.setText(str(save[0][2]))
		self.ui_u.lineEdit_2.setText(str(save[0][3]))
		self.ui_u.lineEdit.setText(str(save[0][4]))
		tun= save[0][5]

	def guardardatos(self):
		con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
		cursor = con.cursor()
		a=self.ui_u.lineEdit_5.toPlainText()
		a1=self.Ui_u.lineEdit_4.toPlainText()
		a2=self.Ui_u.lineEdit_4.toPlainText()
		a3=self.Ui_u.lineEdit_4.toPlainText()
		a4=self.Ui_u.lineEdit_4.toPlainText()
		tun
		cursor.execute("UPDATE Usuarios set idUsuarios= %i, Nombre = %s,Correo = %s,Telefono = %i,Cod_pais = %i WHERE Nombre = %s;"%(int(a),a1,a2,int(tun),int(a4)))
		save = cursor.fetchall()
		cursor.close()
		con.close()
		ida=a1
		U=Ui_Dialog()
		U.showCMessageBox("Usuario actualizado")

	def elimicar(self):
		abc=client()
		item = self.ui_u.lineEdit3.toPlainText()
		prot = "elimicar"
		mess1 = "%s, %s"%(prot,str(item))
		met = mess1
		abc.send(met)

	def mostrarcat(self):
		catr=self.ui_u.comboBox.toPlainText()
		con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
		cursor = con.cursor()
		cursor.execute("SELECT idArticulos,Articulos.Descripcion,stock,precio_unitario,Categoria.Descripcion as 'categoria'  FROM `Tienda Virtual`.Articulos, `Tienda Virtual`.Categoria where Cod_categoria = idCategoria and Categoria.Descripcion='%s';"%(catr))
		save = cursor.fetchall()
		table = MyTableModela(save, self)
		self.ui_u.tiendatable.setModel(table)

	def comprar(self):
		abc=client()
		r = self.ui_u.tiendatable.currentRow()
		field2 = self.ui_u.tiendatable.item(r,1).text()
		field4 = self.ui_u.tiendatable.item(r,3).text()
		prot = "InsertarF"
		mess1 = "%s, %s, %s, %s, %s"%(prot, ida, field2, field4)
		met = mess1
		abc.send(met)


class Dsecundario(QtGui.QDialog):   
	def __init__(self, parent=None):
		super(Dsecundario, self).__init__(parent)
		self.ui_d = Ui_MainWindow()
		self.ui_d.setupUi(self)
		QtCore.QObject.connect(self.ui_d.pushButton, QtCore.SIGNAL("clicked()"), self.insertUs)


	def insertUs(self):
		abc = client()
		prot = "UsuarioI"
		uid = self.ui_d.textEdit.toPlainText()
		nom = self.ui_d.textEdit_2.toPlainText()
		ape = self.ui_d.textEdit_3.toPlainText()
		cor = self.ui_d.textEdit_4.toPlainText()
		tel = self.ui_d.textEdit_5.toPlainText()
		cp = self.ui_d.textEdit_6.toPlainText()
		cps = self.ui_d.textEdit_7.toPlainText()
		contra = self.ui_d.textEdit_8.toPlainText()
		tipo = "2"
		mess1 = "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s"%(prot,uid,nom,ape,cor,tel,cp,cps,contra,tipo)
		met = mess1
		abc.send(met)

class Principal(QtGui.QWidget):
	def __init__(self, parent=None):
		super(Principal, self).__init__(parent)
		self.ui = Ui_Loggin()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.abrirv)
		QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.abrirui)

	def abrirui(self):
		ab = client()
		prot = "Loggin"
		cor = self.ui.textEdit.toPlainText()
		pas = self.ui.textEdit_2.toPlainText()
		mess1 = "%s, %s, %s"%(prot,cor,pas)
		met = mess1
		veri = ab.sendrec(met)
		print veri
		if veri == "1":
			self.d = MainWindou()
			self.d.show()
		elif veri == "2":
			self.ts = Ussa(cor)
			self.ts.show()

	def abrirv(self):
		self.w = Dsecundario()
		self.w.show()

	def quit(self):
		sys.exit(app.exec_())


if __name__ == "__main__":

	app = QtGui.QApplication(sys.argv)
	myapp = Principal()
	myapp.show()
	sys.exit(app.exec_())

