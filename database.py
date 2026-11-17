import mysql.connector
from mysql.connector import Error


class Database:
    """
    Clase encargada de gestionar la conexión
    entre la aplicación y la base de datos MySQL.
    """

    def conectar(self):
        """
        Establece una conexión con la base de datos.
        """
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