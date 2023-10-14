import sys
from GUI import *
from conexionBD import *

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# >>> IMPORTANTE <<<
# LIBRERIAS NECESARIAS EN GUI.py PARA SU FUNCIONAMIENTO (SUSTITUIRLAS POR "PySide2"):
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *


class MiApp(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		
		# CREA INSTANCIA PARA BASE DE DATOS YA CREADA
		self.datosTotal = Registro_datos()
  
		# 1 - PESTAÑA VER TODOS LOS PRODUCTOS
		self.ui.bt_refrescar.clicked.connect(self.m_productos)
		# 2 - PESTAÑA PARA BUSCAR UN PRODUCTO EXISTENTE
		self.ui.bt_buscar.clicked.connect(lambda: self.buscar_producto("PESTAÑA_BUSCAR_PRODUCTO"))
		# 3 - PESTAÑA PARA AGREGAR UN NUEVO PRODUCTO
		self.ui.bt_agregar.clicked.connect(self.insert_productos)
		# 4 - PESTAÑA PARA MODIFICAR UN PRODUCTO EXISTENTE
		self.ui.id_buscar.clicked.connect(lambda: self.buscar_producto("PESTAÑA_MODIFICAR_PRODUCTO"))
		self.ui.bt_actualizar.clicked.connect(self.modificar_producto)
		# 5 - PESTAÑA PARA BORRAR UN PRODUCTO EXISTENTE
		self.ui.borrar_ok.clicked.connect(lambda: self.buscar_producto("PESTAÑA_ELIMINAR_PRODUCTO"))
		self.ui.bt_borrar.clicked.connect(self.eliminar_producto)
  
		
		
	# ----------------------------------------------------------------------------------------------
	def m_productos(self):
		datos = self.datosTotal.buscar_productos()
		i = len(datos)

		self.ui.tabla_productos.setRowCount(i)
		tablerow = 0
		for row in datos:
			self.ui.tabla_productos.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
			self.ui.tabla_productos.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
			self.ui.tabla_productos.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
			self.ui.tabla_productos.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
			self.ui.tabla_productos.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
			
			tablerow += 1
		
		ajustar_columnas(self)
	#-----------------------------------------------------------------------------------------------
	def buscar_producto(self, section):
		# PROCESO DE BUSQUEDA PARA PESTAÑA DE BUSCAR UN PRODUCTO DE NICHO
		if section == "PESTAÑA_BUSCAR_PRODUCTO":
			nombre_producto = self.ui.codigoB.text()
			nombre_producto = str("'" + nombre_producto + "'")

			datosB = self.datosTotal.busca_producto(nombre_producto)
			i = len(datosB)

			self.ui.tabla_buscar.setRowCount(i)
			tablerow = 0
			for row in datosB:
				self.ui.tabla_buscar.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
				self.ui.tabla_buscar.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
				self.ui.tabla_buscar.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
				self.ui.tabla_buscar.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
				self.ui.tabla_buscar.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
	
				tablerow += 1
			ajustar_columnas(self)
		# PROCESO DE BUSQUEDA PARA PESTAÑA PARA MODIFICAR UN PRODCUTO EN EXISTENCIA
		elif section == "PESTAÑA_MODIFICAR_PRODUCTO":
			id_producto = self.ui.id_producto.text()
			id_producto = str("'" + id_producto + "'")
			producto_a_buscar = self.datosTotal.buscar_producto_para_modificar(id_producto)

			if len(producto_a_buscar) == 0: # Producto no encontrado en DB
				print("El producto no existe")
			else: # Si se encuentra lo desglosa poniendolo en las "QLineEdit" Correspondientes de la Pestaña
				self.ui.codigo_actualizar.setText(str(producto_a_buscar[0][0])) # Codigo
				self.ui.nombre_actualizar.setText(str(producto_a_buscar[0][1])) # Nombre
				self.ui.modelo_actualizar.setText(str(producto_a_buscar[0][2])) # Modelo
				self.ui.precio_actualizar.setText(str(producto_a_buscar[0][3])) # Precio
				self.ui.cantidad_actualizar.setText(str(producto_a_buscar[0][4])) # Cantidad
				print("PRODUCTO ENCONTRADO; MODIFIQUE LOS DATOS A DESEAR")
		elif section == "PESTAÑA_ELIMINAR_PRODUCTO":
			nombre_producto = self.ui.codigo_borrar.text()
			nombre_producto = str("'" + nombre_producto + "'")

			datosB = self.datosTotal.buscar_producto_para_modificar(nombre_producto)
			i = len(datosB)

			self.ui.tabla_borrar.setRowCount(i)
			tablerow = 0
			for row in datosB:
				self.ui.tabla_borrar.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
				self.ui.tabla_borrar.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
				self.ui.tabla_borrar.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
				self.ui.tabla_borrar.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
				self.ui.tabla_borrar.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
	
				tablerow += 1
			ajustar_columnas(self)
	#---------------------------------------------------------------------------------------------
	def insert_productos(self):
			codigo = self.ui.codigoA.text()
			nombre = self.ui.nombreA.text()
			modelo = self.ui.modeloA.text()
			precio = self.ui.precioA.text()
			cantidad = self.ui.cantidadA.text()

			self.datosTotal.inserta_producto(codigo, nombre, modelo, precio, cantidad)
			self.ui.codigoA.clear()
			self.ui.nombreA.clear()
			self.ui.modeloA.clear()
			self.ui.precioA.clear()
			self.ui.cantidadA.clear()
	#-----------------------------------------------------------------------------------------------
	def modificar_producto(self):
		codigoM = self.ui.codigo_actualizar.text()
		nombreM = self.ui.nombre_actualizar.text()
		modeloM = self.ui.modelo_actualizar.text()
		precioM = self.ui.precio_actualizar.text()
		cantidadM = self.ui.cantidad_actualizar.text()
		
		# Llama a la Funcion para Actualizar los Productos en la Data Base
		self.datosTotal.actualiza_productos(codigoM, nombreM, modeloM, precioM, cantidadM, self.ui.id_producto.text())
		
		print("PRODUCTOS ACTUALIZADOS CORRECTAMENTE")
		self.ui.codigo_actualizar.clear()
		self.ui.nombre_actualizar.clear()
		self.ui.modelo_actualizar.clear()
		self.ui.precio_actualizar.clear()
		self.ui.cantidad_actualizar.clear()
		self.ui.id_producto.clear()
	#-----------------------------------------------------------------------------------------------
	def eliminar_producto(self):
		eliminar = self.ui.codigo_borrar.text()
		eliminar = str("'" + eliminar + "'")
		self.datosTotal.elimina_producto(eliminar)
		print("PRODUCTO ELIMINADO CON EXITO")
#----------------------------------------------------------------------------------------------------
def ajustar_columnas(self):
	# Ajustar Columnas
	self.ui.tabla_productos.resizeColumnsToContents()
	self.ui.tabla_borrar.resizeColumnsToContents()
	self.ui.tabla_buscar.resizeColumnsToContents()


#####################################################################################################
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())
