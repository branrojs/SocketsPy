import socket
import sys
import MySQLdb
import datetime
class mysocket:
	def __init__(self):
		server = socket.socket()
		global addres 
		addres = ("127.0.0.1",1237)
		server.bind(addres)
		server.listen(7)
		global count
		count = 0
		while True:
			print "Iniciando servidor "
			client, addr = server.accept()
			print "Cliente conectando desde: ", addr[0],":",addr[1]
			while True:
				data = client.recv(1024)
				datos = data.split(", ")
				if datos[0]=="UsuarioI":
					con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
					cursor = con.cursor()
					try:
						cursor.callproc('InsertarU',(int(datos[1]),datos[2],datos[3],datos[4],int(datos[5]),int(datos[6]),int(datos[7]),datos[8],int(datos[9])))
						con.commit()
					except MySQLdb.Error as e:
						try:
							print "MySQL ERROR [%d]: %s" %(e.args[0], e.args[1])
						except IndexError:
							print "MySQL Error %s" % str(e)
					finally:
						client.send("Trans completada")
						cursor.close()
						con.close()
				elif(datos[0]=="UsuarioU"):
					con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
					cursor = con.cursor()
					try:
						cursor.callproc('Updateu',(int(datos[1]),datos[2],datos[3],datos[4],int(datos[5]),int(datos[6]),int(datos[7]),datos[8],int(datos[9])))
						con.commit()
					except MySQLdb.Error as e:
						try:
							print "MySQL ERROR [%d]: %s" %(e.args[0], e.args[1])
						except IndexError:
							print "MySQL Error %s" % str(e)
					finally:
						client.send("Trans completada")
						cursor.close()
						con.close()
				elif(datos[0]=="insertarA"):
					con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
					cursor = con.cursor()
					try:
						cursor.callproc('insertA',(int(datos[1]),datos[2],int(datos[3]),float(datos[4]),int(datos[5])))
						con.commit()

					except MySQLdb.Error as e:
						try:
							print "MySQL ERROR [%d]: %s" %(e.args[0], e.args[1])
						except IndexError:
							print "MySQL Error %s" % str(e)
					finally:
						client.send("Trans completada")
						cursor.close()
						con.close()
				elif(datos[0]=="Insertarad"):
					con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
					cursor = con.cursor()
					try:
						cursor.callproc('insertar_amd',(datos[1],int(datos[2]),datos[3]))
						con.commit()
					except MySQLdb.Error as e:
						try:
							print "MySQL ERROR [%d]: %s" %(e.args[0], e.args[1])
						except IndexError:
							print "MySQL Error %s" % str(e)
					finally:
						client.send("Trans completada")
						cursor.close()
						con.close()
				elif(datos[0]=="InsertarF"):
					con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
					cursor = con.cursor()
					try:
						hoy=datetime.date.today()
						cursor.callproc('InsertarF',(int(datos[1]),str(hoy),float(datos[3]),str(datos[2])))
						con.commit()
						cursor.execute('SELECT * FROM Articulos where Descripcion=%s'%(str(datos[2])))
						num= cursor.fetchone()
						decree = int(num[2])
						decree = decree-1
						cursor.execute('UPDATE Articulos Set stock=%i where Descripcion=%s'%(decree,str(datos[2])))
						con.commit()
					except MySQLdb.Error as e:
						try:
							print "MySQL ERROR [%d]: %s" %(e.args[0], e.args[1])
						except IndexError:
							print "MySQL Error %s" % str(e)
					finally:
						cursor.close()
						con.close()
				elif(datos[0]=="UpdateA"):
					con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
					cursor = con.cursor()
					try:
						cursor.callproc('UpdateA',(int(datos[1]),datos[2],int(datos[3]),float(datos[4]),int(datos[5])))
						con.commit()
					except MySQLdb.Error as e:
						try:
							print "MySQL ERROR [%d]: %s" %(e.args[0], e.args[1])
						except IndexError:
							print "MySQL Error %s" % str(e)
					finally:
						client.send("Trans completada")
						cursor.close()
						con.close()
				elif(datos[0]=="Updatead"):
					con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
					cursor = con.cursor()
					try:
						cursor.callproc('Update_amd',(datos[1],int(datos[2]),datos[3]))
						con.commit()
					except MySQLdb.Error as e:
						try:
							print "MySQL ERROR [%d]: %s" %(e.args[0], e.args[1])
						except IndexError:
							print "MySQL Error %s" % str(e)
					finally:
						client.send("Trans completada")
						cursor.close()
						con.close()
				elif(datos[0]=="UpdateF"):
					con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
					cursor = con.cursor()
					try:
						cursor.callproc('UpdateF',(int(datos[1]),int(datos[2]),int(datos[3]),float(datos[4])))
						con.commit()
					except MySQLdb.Error as e:
						try:
							print "MySQL ERROR [%d]: %s" %(e.args[0], e.args[1])
						except IndexError:
							print "MySQL Error %s" % str(e)
					finally:
						client.send("Trans completada")
						cursor.close()
						con.close()
				elif(datos[0]=="Eliminar"):
					con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
					cursor = con.cursor()
					try:
						cursor.callproc('DeletGlobal',(datos[1],int(datos[2])))
						con.commit()
					except MySQLdb.Error as e:
						try:
							print "MySQL ERROR [%d]: %s" %(e.args[0], e.args[1])
						except IndexError:
							print "MySQL Error %s" % str(e)
						break 
					finally:
						client.send("Trans completada")
						cursor.close()
						con.close()
				elif(datos[0]=="Loggin"):
					con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
					cursor = con.cursor()
					try:
						
						cursor.execute("SELECT * FROM Usuarios where Nombre = '%s'"%(datos[1]))
						save = cursor.fetchall()
						if datos[1]==save[0][1]:
							if datos[2]==save[0][7]:
								print "Llegue"
								if save[0][8]==1:
									client.send("1")
								elif save[0][8]==2:
									client.send("2")
							else:
								client.send("Password o Nick incorrecta")
						else:
							client.send("Password o Nick incorrecta")
					except MySQLdb.Error as e:
						try:
							print "MySQL ERROR [%d]: %s" %(e.args[0], e.args[1])
						except IndexError:
							print "MySQL Error %s" % str(e)
						break
					finally:
						cursor.close()
						con.close()
				elif(datos[0]=="elimicar"):
					con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
					cursor = con.cursor()
					try:
						cursor.execute("DELETE FROM Carrito WHERE `idCarrito`=%i;"%(int(datos[1])))
						con.commit()
					except MySQLdb.Error as e:
						try:
							print "MySQL ERROR [%d]: %s" %(e.args[0], e.args[1])
						except IndexError:
							print "MySQL Error %s" % str(e)
					finally:
						client.send("Trans completada")
						cursor.close()
						con.close()
				elif(datos[0]=="agregacar"):
					con = MySQLdb.connect('localhost','root','oveja','Tienda Virtual')
					cursor = con.cursor()
					try: ################quedaste aca maricon
						cursor.execute("INSERT INTO Facturacion(idFacturacion,User_id,fecha,precio_total, nombrart)VALUES ( Default ,%i ,'",datos[2],"' ,%f);"%(int(datos[1]),float(datos[3])))
						con.commit()
					except MySQLdb.Error as e:
						try:
							print "MySQL ERROR [%d]: %s" %(e.args[0], e.args[1])
						except IndexError:
							print "MySQL Error %s" % str(e)
					finally:
						client.send("Trans completada")
						cursor.close()
						con.close()
				elif(datos[0]=="Fin"):
					print "Cliente saliendo desde: ", addr[0],":",addr[1]
					break


if __name__ == "__main__":

	u=mysocket()
	u()
