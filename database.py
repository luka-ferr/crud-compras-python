import mysql.connector
from mysql.connector import Error


class Database:

    def conectar(self):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="crud_compras"
            )

            if conexion.is_connected():
                return conexion

        except Error as error:
            print("Error al conectar con MySQL:", error)

        return None