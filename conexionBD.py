import sqlite3


class Registro_datos():
    def __init__(self):
        self.conexion = sqlite3.connect(
            "DB.db")  # Conexión a DB
    #-----------------------------------------------------------------------------------------------
    def buscar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos "
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro
    #----------------------------------------------------------------------------------------------
    def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombrex = cur.fetchall()
        cur.close()
        return nombrex
    #-----------------------------------------------------------------------------------------------
    def inserta_producto(self, codigo, nombre, modelo, precio, cantidad):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO productos (CODIGO, NOMBRE, MODELO, PRECIO, CANTIDAD) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(codigo, nombre, modelo, precio, cantidad)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
    #-----------------------------------------------------------------------------------------------
    def actualiza_productos(self, codigo, nombre, modelo, precio, cantidad, codigo_anterior):
        cur = self.conexion.cursor()
        sql = '''UPDATE productos SET
            CODIGO = ?, NOMBRE = ?, MODELO = ?, PRECIO = ?, CANTIDAD = ? WHERE CODIGO = ?'''
        valores = (codigo, nombre, modelo, precio, cantidad, codigo_anterior)
        cur.execute(sql, valores)
        act = cur.rowcount
        self.conexion.commit()
        cur.close()
        return act
    #-----------------------------------------------------------------------------------------------
    def elimina_producto(self, codigo):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM productos WHERE CODIGO = {}'''.format(codigo)
        cur.execute(sql)
        nom = cur.rowcount
        self.conexion.commit()
        cur.close()
        return nom

    def buscar_producto_para_modificar(self, codigo_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE CODIGO = {}".format(codigo_producto)
        cur.execute(sql)
        nombrex = cur.fetchall()
        cur.close()
        return nombrex
