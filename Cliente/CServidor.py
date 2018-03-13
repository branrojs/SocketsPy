import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from zoket import client
import MySQLdb
import string


class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

class Ui_Dialog(object):
    def showEMessageBox(self,message):
            msg = QMessageBox()
            msq.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Error")
            msg.setInformativeText(message)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def showCMessageBox(self,message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Error")
        msg.setInformativeText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
################# Todo lo de articulos Aca abajo###################
class listaa(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        artitable = QTableView()
        layout = QHBoxLayout()
        layout.addWidget(artitable)
        con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
        cursor = con.cursor()
        cursor.execute("SELECT idArticulos, Articulos.Descripcion, stock, precio_unitario, Categoria.Descripcion  FROM Articulos, Categoria WHERE Cod_categoria = idCategoria;")
        save = cursor.fetchall()
        tablemodel = MyTableModel(save, self)
        artitable.setModel(tablemodel)
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Lista de articulos")

class agregara(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        global cod, desc, st,pre,cat
        l1 = QLabel("Codigo de Articulo")
        cod = QTextEdit()
        l2 = QLabel("Descripcion")
        desc = QTextEdit()
        l3 = QLabel("Cantidads")
        st = QTextEdit()
        l4 = QLabel("Precio")
        pre = QTextEdit()
        l5 = QLabel("Categoria")
        cat = QTextEdit()
        fbox = QFormLayout()
        fbox.addRow(l1,cod)
        fbox.addRow(l2,desc)
        fbox.addRow(l3,st)
        fbox.addRow(l4,pre)
        fbox.addRow(l5,cat)
        button1 = QPushButton("Agregar")
        fbox.addRow(button1)
        self.connect(button1, SIGNAL('clicked()'), self.inserta)
        self.widget = QWidget()
        self.widget.setLayout(fbox)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Agregar articulos")

    def inserta(self):
        abc = client()
        prot = "insertarA"
        uid = cod.toPlainText()
        nm =  desc.toPlainText()
        ape= st.toPlainText()
        cor= pre.toPlainText()
        tel= cat.toPlainText()
        ms = Ui_Dialog()
        if(str(uid).isalpha() or uid == "" or int(uid)<0):
            ms.showEMessageBox("Id no puede contener letras o estar vacio y no puede ser menor a 0")
        elif(nm==""):
            ms.showEMessageBox("Descripcion vacio")
        elif(ape==""):
            ms.showEMessageBox("Cantidad vacio, tiene letras o es menor a 0")
        elif(str(cor).isalpha() or cor=="" or int(cor)<0):
            ms.showEMessageBox("el precio esta vacio, tiene letras o es menor a 0")
        elif(str(tel).isalpha() or tel=="" or int(tel)<0):
            ms.showEMessageBox("la categoria esta vacio o tiene alguna letra en su contenedor y no puede ser menor a 0")
        else:
            mess1 = "%s, %s, %s, %s, %s, %s"%(prot,uid,nm,ape,cor,tel)
            met = mess1
            abc.send(met)
            ms.showCMessageBox("Exito")

class editara(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        global cod, desc, st,pre,cat
        l1 = QLabel("Codigo de Articulo")
        cod = QTextEdit()
        l2 = QLabel("Descripcion")
        desc = QTextEdit()
        l3 = QLabel("Stock")
        st = QTextEdit()
        l4 = QLabel("Precio")
        pre = QTextEdit()
        l5 = QLabel("Categoria")
        cat = QTextEdit()
        fbox = QFormLayout()
        fbox.addRow(l1,cod)
        fbox.addRow(l2,desc)
        fbox.addRow(l3,st)
        fbox.addRow(l4,pre)
        fbox.addRow(l5,cat)
        p1 = QPushButton("Actualizar")
        fbox.addRow(p1)
        self.connect(p1, SIGNAL('clicked()'), self.actuar)
        self.widget = QWidget()
        self.widget.setLayout(fbox)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Editar articulos")

    def actuar(self):
        abc = client()
        prot = "UpdateA"
        uid = cod.toPlainText()
        nm =  desc.toPlainText()
        ape= st.toPlainText()
        cor= pre.toPlainText()
        tel= cat.toPlainText()
        ms= Ui_Dialog()
        if(str(uid).isalpha() or uid == "" or int(uid)<0):
            ms.showEMessageBox("Id no puede contener letras o estar vacio y no puede ser menor a 0")
        elif(nm==""):
            ms.showEMessageBox("Descripcion vacio")
        elif(ape==""):
            ms.showEMessageBox("Cantidad vacio, tiene letras o es menor a 0")
        elif(str(cor).isalpha() or cor=="" or int(cor)<0):
            ms.showEMessageBox("el precio esta vacio, tiene letras o es menor a 0")
        elif(str(tel).isalpha() or tel=="" or int(tel)<0):
            ms.showEMessageBox("la categoria esta vacio o tiene alguna letra en su contenedor y no puede ser menor a 0")
        else:
            mess1 = "%s, %s, %s, %s, %s, %s"%(prot,uid,nm,ape,cor,tel)
            met = mess1
            abc.send(met)
            ms.showCMessageBox("Articulo Actualizad@")

class eliminara(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        l1 = QLabel("Codigo de Articulo")
        cod = QTextEdit()
        fbox = QFormLayout()
        fbox.addRow(l1,cod)
        button = QPushButton("Eliminar")
        fbox.addRow(button)
        self.connect(button, SIGNAL('clicked()'), self.elia)
        self.widget = QWidget()
        self.widget.setLayout(fbox)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Eliminar articulos")

    def elia(self):
        abc = client()
        prot = "Eliminar"
        prot2 = "Artic"
        ed=cod.toPlainText()
        ms= Ui_Dialog()
        if(str(ed).isalpha() or ed == "" or int(ed)<0):
            ms.showEMessageBox("Id no puede contener letras o estar vacio o ser menor a 0")
        else:
             mess1 = "%s, %s, %s"%(prot,prot2,ed)
             met = mess1
             abc.send(met)
             ms.showCMessageBox("Usuario Eliminao!!!! FOREVA!")

class articulos(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        layout = QHBoxLayout()

        button = QPushButton("Lista de articulos disponibles")
        button2 = QPushButton("Agregar articulos")
        button3 = QPushButton("Editar articulos")
        button4 = QPushButton("Eliminar articulos")

        layout.addWidget(button)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)

        self.widget = QWidget()
        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)
        self.setWindowTitle("Administrar Articulos")
        self.connect(button, SIGNAL('clicked()'), self.listaa)
        self.connect(button2, SIGNAL('clicked()'), self.agregara)
        self.connect(button3, SIGNAL('clicked()'), self.editara)
        self.connect(button4, SIGNAL('clicked()'), self.eliminara)

    def listaa(self):
    	self.mylista = listaa()
    	self.mylista.show()

    def agregara(self):
    	self.myadda = agregara()
    	self.myadda.show()

    def editara(self):
    	self.myedita = editara()
    	self.myedita.show()

    def eliminara(self):
    	self.mydeleta = eliminara()
    	self.mydeleta.show()


################# aca para arriba ^ articulos#########
################# Todo lo de ventas Aca abajo###################
class registro_ventas(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        ventastable = QTableView()
        layout = QHBoxLayout()
        layout.addWidget(ventastable)
        con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
        cursor = con.cursor()
        cursor.execute("SELECT idFacturacion as '#Factura', Fecha, nombrart as 'Articulo Vendido', Precio_total as 'Precio Unitario', Nombre as 'Comprador', idUsuarios as 'id'  FROM Facturacion,Usuarios where User_id = idUsuarios;")
        save = cursor.fetchall()
        tablemodel = MyTableModel(save, self)
        ventastable.setModel(tablemodel)
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Registro de ventas")

class ventas_por_categoria(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        global buscar, Ventasxc
        button = QPushButton("Buscar")
        buscar= QTextEdit()
        con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
        Ventasxc= QTableView()
        layout = QHBoxLayout()
        layout.addWidget(Ventasxc)
        leyout = QVBoxLayout()
        leyout.addWidget(button)
        leyout.addWidget(buscar)
        layout.addLayout(leyout)
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Ventas por Categoria")
        self.connect(button, SIGNAL('clicked()'), self.llenartablita)

    def llenartablita(self):
        con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
        cursor = con.cursor()
        tent = buscar.toPlainText()
        cursor.execute("SELECT idFacturacion as '#Factura', Fecha, nombrart as 'Articulo Vendido', Precio_total as 'Precio Unitario', Nombre as 'Comprador', idUsuarios as 'id' FROM Facturacion, Articulos, Usuarios, Categoria where  nombrart=Articulos.Descripcion AND User_id = idUsuarios and Categoria.Descripcion = '%s';"%(tent))
        save = cursor.fetchall()
        tablemodel = MyTableModel(save, self)
        Ventasxc.setModel(tablemodel)

class ventas(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        layout = QHBoxLayout()
        button = QPushButton("Registro de ventas")
        button2= QPushButton("Registro de ventas por categoria")
        layout.addWidget(button)
        layout.addWidget(button2)
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Ventas")
        self.connect(button, SIGNAL('clicked()'), self.registro)
        self.connect(button2, SIGNAL('clicked()'), self.registroc)

    def registro(self):
    	self.myreg = registro_ventas()
    	self.myreg.show()

    def registroc(self):
    	self.myregc = ventas_por_categoria()
    	self.myregc.show()

################# aca para arriba ^ Ventas#########
################# Todo lo de Usuarios Aca abajo###################
class listac(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.widget = QWidget()
        cattable = QTableView()
        layout = QHBoxLayout()
        layout.addWidget(cattable)
        con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Categoria;")
        save = cursor.fetchall()
        tablemodel = MyTableModel(save, self)
        cattable.setModel(tablemodel)
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Lista de categorias")

class agregarc(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        global cod, desc
        l1 = QLabel("Codigo de Categoria")
        cod = QTextEdit()
        l2 = QLabel("Descripcion")
        desc = QTextEdit()
        fbox = QFormLayout()
        fbox.addRow(l1,cod)
        fbox.addRow(l2,desc)
        button1= QPushButton("Agregar")
        fbox.addRow(button1)
        self.connect(button1, SIGNAL('clicked()'), self.insertc) 

        self.widget = QWidget()
        self.widget.setLayout(fbox)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Agregar categoria")

    def insertc(self):
        abc = client()
        prot = "Insertarad"
        prot2 = "Categoria"
        de=cod.toPlainText()
        dcp=desc.toPlainText()
        ms= Ui_Dialog()
        if(str(de).isalpha() or int(de)<0 or de==""):
            ms.showEMessageBox("Id no puede contener letras ni ser menor a 0")
        elif(dcp==""):
            ms.showEMessageBox("La descripcion esta vacia")
        else:
            mess1 = "%s, %s, %s, %s"%(prot,prot2,de,dcp)
            met = mess1
            abc.send(met)
            ms.showCMessageBox("Exito")

class editarc(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        global cod, cod1,desc
        l1 = QLabel("Codigo de Categoria Viejo")
        cod = QTextEdit()
        l2 = QLabel("Descripcion Nueva")
        desc = QTextEdit()
        fbox = QFormLayout()
        fbox.addRow(l1,cod)
        fbox.addRow(l2,desc)
        p1 = QPushButton("Actualizar")
        fbox.addRow(p1)
        self.connect(p1, SIGNAL('clicked()'), self.actuC)
        self.widget = QWidget()
        self.widget.setLayout(fbox)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Editar categoria")

    def actuC(self):
        abc = client()
        prot = "Updatead"
        prot2 = "Categoria"
        ed=cod.toPlainText()
        de = ed 
        dcp=desc.toPlainText()
        ms= Ui_Dialog()
        if(str(de).isalpha() or int(de)<0 or de==""): 
            ms.showEMessageBox("Id no puede contener letras ni ser menor a 0")
        elif(dcp==""):
            ms.showEMessageBox("La descripcion esta vacia")
        else:
            mess1 = "%s, %s, %s, %s"%(prot,prot2,ed,dcp)
            met = mess1
            abc.send(met)
            ms.showCMessageBox("Categoria Actualizada")
class eliminarc(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        global cod
        l1 = QLabel("Codigo de Categoria")
        cod = QTextEdit()
        fbox = QFormLayout()
        fbox.addRow(l1,cod)
        button = QPushButton("Eliminar")
        fbox.addRow(button)
        self.widget = QWidget()
        self.widget.setLayout(fbox)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Eliminar categoria")
        self.connect(button, SIGNAL('clicked()'), self.elic)

    def elic(self):
        abc = client()
        prot = "Eliminar"
        prot2 = "Categoria"
        ed=cod.toPlainText()
        ms= Ui_Dialog()
        if(str(ed).isalpha() or ed == "" or int(ed)<0):
            ms.showEMessageBox("Id no puede contener letras o estar vacio o ser menor a 0")
        else:
             mess1 = "%s, %s, %s"%(prot,prot2,ed)
             met = mess1
             abc.send(met)
             ms.showCMessageBox("Usuario Eliminao!!!! FOREVA!")

class Categorias(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        layout = QHBoxLayout()
       
        button = QPushButton("Lista de categorias disponibles")
        button2 = QPushButton("Agregar categorias")
        button3 = QPushButton("Editar categorias")
        button4 = QPushButton("Eliminar categorias")

        layout.addWidget(button)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)

        self.widget = QWidget()
        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)
        self.setWindowTitle("Categorias")

        self.connect(button, SIGNAL('clicked()'), self.listac)
        self.connect(button2, SIGNAL('clicked()'), self.agregarc)
        self.connect(button3, SIGNAL('clicked()'), self.editarc)
        self.connect(button4, SIGNAL('clicked()'), self.eliminarc)

    def listac(self):
    	self.mylistc = listac()
    	self.mylistc.show()

    def agregarc(self):
    	self.myaddc = agregarc()
    	self.myaddc.show()

    def editarc(self):
    	self.myeditc = editarc()
    	self.myeditc.show()

    def eliminarc(self):
    	self.mydeletc = eliminarc()
    	self.mydeletc.show()

################# aca para arriba ^ categorias#########
################# Todo lo de Usuarios Aca abajo###################
class listau(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.widget = QWidget()
        clientetable = QTableView()
        layout = QHBoxLayout()
        layout.addWidget(clientetable)
        con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
        cursor = con.cursor()
        cursor.execute("SELECT idUsuarios, Nombre, Apellidos, Correo, Telefono, Descrip as 'Pais', Cod_postal as 'Codigo postal' , Descripcion as 'Tipo Usuario' FROM Usuarios, Pais, Tipo_usuario where cod_pais = idPais and Tipo_usuario = Cod_Tipo_Usuario;")
        save = cursor.fetchall()
        tablemodel = MyTableModel(save, self)
        clientetable.setModel(tablemodel)
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Lista de usuarios")

class agregaru(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        l1 = QLabel("Cedula")
        global ida, nom, ap, corr, telf, tip, pais, cod, contr 
        ida= QTextEdit()
        l2 = QLabel("Nombre")
        nom = QTextEdit()
        l3 = QLabel("Apellido")
        ap = QTextEdit()
        l4 = QLabel("Correo")
        corr = QTextEdit()
        l10 = QLabel("Telefono")
        telf = QTextEdit()
        l5 = QLabel("Tipo de Usuario")
        tip = QTextEdit()
        l6 = QLabel("Pais")
        pais = QTextEdit()
        l7 = QLabel("Codigo Postal")
        cod = QTextEdit()
        l8 = QLabel("Contrasena")
        contr = QTextEdit()
        fbox = QFormLayout()
        fbox.addRow(l1,ida)
        vbox = QVBoxLayout()
        vbox.addWidget(nom)
        fbox.addRow(l2,vbox)
        fbox.addRow(l3,ap)
        fbox.addRow(l4,corr)
        fbox.addRow(l10,telf)
        fbox.addRow(l5,tip)
        fbox.addRow(l6,pais)
        fbox.addRow(l7,cod)
        fbox.addRow(l8,contr)
        button1 = QPushButton("Registrar")
        fbox.addRow(button1)

        self.widget = QWidget()
        self.widget.setLayout(fbox)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Agregar usuarios")
        self.connect(button1, SIGNAL('clicked()'), self.insertt)    

    def insertt(self):
        abc = client()
        prot = "UsuarioI"
        uid = ida.toPlainText()
        nm =  nom.toPlainText()
        ape= ap.toPlainText()
        cor= corr.toPlainText()
        tel =  telf.toPlainText()
        cp= pais.toPlainText()
        cps= cod.toPlainText()
        contra =  contr.toPlainText()
        tipo= tip.toPlainText()
        ms= Ui_Dialog()
        if(str(uid).isalpha() or uid == ""):
            ms.showEMessageBox("Id no puede contener letras o estar vacio")
        elif(nm==""):
            ms.showEMessageBox("el Nombre esta vacio")
        elif(ape==""):
            ms.showEMessageBox("el apellido esta vacio")
        elif(cor==""):
            ms.showEMessageBox("el correo esta vacio")
        elif(str(tel).isalpha() or tel=="" or int(tel)<0):
            ms.showEMessageBox("el telefono esta vacio o tiene alguna letra en su contenedor o es menor a 0")
        elif(str(cp).isalpha() or cp=="" or int(cp)<0):
            ms.showEMessageBox("el codigo pais esta vacio o tiene letras en su contenedor o es menor a 0")
        elif(str(cps).isalpha() or cps=="" or int(cps)<0):
            ms.showEMessageBox("Codigo postal esta vacio, tiene letras o es menor a 0")
        elif(contra==""):
            ms.showEMessageBox("Password esta vacio")
        elif(str(tipo).isalpha() or tipo=="" or int(tipo)<0):
            ms.showEMessageBox("el tipo esta vacio o tiene letras en su contenedor")
        else:
            mess1 = "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s"%(prot,uid,nm,ape,cor,tel,cp,cps,contra,tipo)
            met = mess1
            abc.send(met)
            ms.showCMessageBox("Usuario Actualizad@")

class editaru(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        global ced, nom, ap, corr, tip, pais, cod, contr,telf
        l1 = QLabel("Cedula")
        ced = QTextEdit()
        l2 = QLabel("Nombre")
        nom = QTextEdit()
        l3 = QLabel("Apellido")
        ap = QTextEdit()
        l4 = QLabel("Correo")
        corr = QTextEdit()
        l5 = QLabel("Tipo de Usuario")
        tip = QTextEdit()
        l6 = QLabel("Pais")
        pais = QTextEdit()
	l7 = QLabel("Codigo Postal")
        cod = QTextEdit()
        l8 = QLabel("Contrasena")
        contr = QTextEdit()
	l9 = QLabel("Telefono")
        telf = QTextEdit()
        fbox = QFormLayout()
        fbox.addRow(l1,ced)
        vbox = QVBoxLayout()
        vbox.addWidget(nom)
        fbox.addRow(l2,vbox)
        fbox.addRow(l3,ap)
        fbox.addRow(l4,corr)
        fbox.addRow(l9,telf)
        fbox.addRow(l5,tip)
        fbox.addRow(l6,pais)
        fbox.addRow(l7,cod)
        fbox.addRow(l8,contr)
        p1 = QPushButton("Actualizar")
        fbox.addRow(p1)
        self.connect(p1, SIGNAL('clicked()'), self.actu)
        self.widget = QWidget()
        self.widget.setLayout(fbox)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Editar Usuarios")

    def actu(self):
        abc = client()
        prot = "UsuarioU"
        uid = ced.toPlainText()
        nm =  nom.toPlainText()
        ape= ap.toPlainText()
        cor= corr.toPlainText()
        tel =  telf.toPlainText()
        cp= pais.toPlainText()
        cps= cod.toPlainText()
        contra =  contr.toPlainText()
        tipo= tip.toPlainText()
        ms= Ui_Dialog()
        if(str(uid).isalpha() or uid == ""):
            
            ms.showEMessageBox("Id no puede contener letras o estar vacio")
        elif(nm==""):
            ms.showEMessageBox("el Nombre esta vacio")
        elif(ape==""):
            ms.showEMessageBox("el apellido esta vacio")
        elif(cor==""):
            ms.showEMessageBox("el correo esta vacio")
        elif(str(tel).isalpha() or tel=="" or int(tel)<0):
            ms.showEMessageBox("el telefono esta vacio o tiene alguna letra en su contenedor o es menor a 0")
        elif(str(cp).isalpha() or cp=="" or int(cp)<0):
            ms.showEMessageBox("el codigo pais esta vacio o tiene letras en su contenedor o es menor a 0")
        elif(str(cps).isalpha() or cps=="" or int(cps)<0):
            ms.showEMessageBox("Codigo postal esta vacio, tiene letras o es menor a 0")
        elif(contra==""):
            ms.showEMessageBox("Password esta vacio")
        elif(str(tipo).isalpha() or tipo=="" or int(tipo)<0):
            ms.showEMessageBox("el tipo esta vacio o tiene letras en su contenedor")
        else:
            mess1 = "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s"%(prot,uid,nm,ape,cor,tel,cp,cps,contra,tipo)
            met = mess1
            abc.send(met)
            ms.showCMessageBox("Usuario Actualizad@")

class eliminaru(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        global ced,nom, ap
        l1 = QLabel("Cedula")
        ced = QTextEdit()
        fbox = QFormLayout()
        fbox.addRow(l1,ced)
        button = QPushButton("Eliminar")
        fbox.addRow(button)
        self.widget = QWidget()
        self.widget.setLayout(fbox)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Eliminar usuarios")
        self.connect(button, SIGNAL('clicked()'), self.eliu)

    def eliu(self):
        abc = client()
        prot = "Eliminar"
        prot2 = "User"
        ed=ced.toPlainText()
        ms= Ui_Dialog()
        if(str(ed).isalpha() or ed == "" or int(ed)<0):
            ms.showEMessageBox("Id no puede contener letras o estar vacio o ser menor a 0")
        else:
             mess1 = "%s, %s, %s"%(prot,prot2,ed)
             met = mess1
             abc.send(met)
             ms.showCMessageBox("Usuario Eliminao!!!! FOREVA!")

class Client(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        layout = QHBoxLayout()
        lineEdit = QTextEdit()
        button = QPushButton("Ver lista de Usuarios")
        button2 = QPushButton("Agregar Usuario Nuevo")
        button3 = QPushButton("Editar Usuarios")
        button4 = QPushButton("Eliminar Usuarios")
        layout.addWidget(button)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)


        self.widget = QWidget()
        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)
        self.setWindowTitle("Aministrador de usuarios")

        self.connect(button, SIGNAL('clicked()'), self.listau)
        self.connect(button2, SIGNAL('clicked()'), self.agregaru)
        self.connect(button3, SIGNAL('clicked()'), self.editaru)
        self.connect(button4, SIGNAL('clicked()'), self.eliminaru)

    def listau(self):
    	self.mylistu = listau()
    	self.mylistu.show()

    def agregaru(self):
    	self.myaddu = agregaru()
    	self.myaddu.show()

    def editaru(self):
    	self.myeditu = editaru()
    	self.myeditu.show()

    def eliminaru(self):
    	self.mydeletu = eliminaru()
    	self.mydeletu.show()
      
################Usuarios de ^ ##############################
##############Todo lo de la main windown V abajo############
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        layout = QVBoxLayout()
        button = QPushButton("Administrar Usuarios")
        button2 = QPushButton("Administrar Articulos")
        button3 = QPushButton("Administrar Categorias")
        button4 = QPushButton("Administrar Ventas")
        layout.addWidget(button)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)

        self.widget = QWidget()
        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)
        self.setWindowTitle("Servidor")

        self.connect(button, SIGNAL('clicked()'), self.newWindow)
        self.connect(button2, SIGNAL('clicked()'), self.newWindow2)
        self.connect(button3, SIGNAL('clicked()'), self.newWindow3)
        self.connect(button4, SIGNAL('clicked()'), self.newWindow4)

    def newWindow(self):
        self.myClient = Client()
        self.myClient.show()

    def newWindow2(self):
        self.misArticulos = articulos()
        self.misArticulos.show()

    def newWindow3(self):
        self.myCats = Categorias()
        self.myCats.show()

    def newWindow4(self):
        self.myvent = ventas()
        self.myvent.show()
############# de aca para ^ main windown y abajo el Main func##########
if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setGeometry(200, 200, 200, 200)
    mainWindow.show()
    sys.exit(app.exec_()) #Funcion Main :)
