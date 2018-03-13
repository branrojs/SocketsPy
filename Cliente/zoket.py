import sys
import socket

class client:
	def __init__(self):
		ip = '127.0.0.1'
		port = 1237
		global addres
		addres=(ip,port)

	def send(self,mensaje):
		client = socket.socket()
		client.connect(addres)
		client.send(mensaje)
		me=client.recv(1024)
		client.send("Fin")
		client.close()

	def sendrec(self,mensaje):
		client = socket.socket()
		client.connect(addres)
		client.send(mensaje)
		me=client.recv(1024)
		print me
		client.send("Fin")
		client.close()
		return me

	def sendfin(self):
		client = socket.socket()
		client.connect(addres)
		client.send("Fin")
		client.close()