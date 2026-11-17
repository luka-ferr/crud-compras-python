from database import Database
from compra import Compra


class CompraCRUD:
    """
    Clase encargada de realizar las operaciones CRUD
    sobre la tabla compra de la base de datos.
    """

    def __init__(self):
        self.database = Database()

    # REGISTRAR COMPRA
    def registrar_compra(self, compra):
        """
        Registra una nueva compra en la base de datos.

        Args:
            compra (Compra): objeto que contiene los datos
            del producto, cantidad y precio.
        """

        # Establece la conexión con la base de datos.
        conexion = self.database.conectar()

        if conexion is None:
            return

        cursor = None

        try:
            cursor = conexion.cursor()

            sql = """
                INSERT INTO compra (producto, cantidad, precio)
                VALUES (%s, %s, %s)
            """

            valores = (
                compra.producto,
                compra.cantidad,
                compra.precio
            )

            cursor.execute(sql, valores)
            conexion.commit()

            print("\n¡Compra registrada correctamente!")
            print("ID generado:", cursor.lastrowid)

        except Exception as error:
            print("Error al registrar la compra:", error)

        finally:
            if cursor:
                cursor.close()

            conexion.close()

    # CONSULTAR COMPRAS
    def consultar_compras(self):
        """
        Consulta todos los registros existentes en la tabla compra.

        Returns:
            list: lista de objetos Compra con los datos consultados.
            []: lista vacía si no existen registros o hay un error.
        """

        conexion = self.database.conectar()

        if conexion is None:
            return []

        cursor = None

        try:
            cursor = conexion.cursor()

            sql = """
                SELECT id, producto, cantidad, precio
                FROM compra
            """

            cursor.execute(sql)

            resultados = cursor.fetchall()

            compras = []

            for fila in resultados:

                compra = Compra(
                    id=fila[0],
                    producto=fila[1],
                    cantidad=fila[2],
                    precio=float(fila[3])
                )

                compras.append(compra)

            return compras

        except Exception as error:
            print("Error al consultar las compras:", error)
            return []

        finally:
            if cursor:
                cursor.close()

            conexion.close()

    # ACTUALIZAR COMPRA
    def actualizar_compra(self, id_compra, producto, cantidad, precio):
        """
        Actualiza los datos de una compra existente.

        Args:
            id_compra: identificador de la compra que se actualizará.
            producto: nuevo nombre del producto.
            cantidad: nueva cantidad de unidades.
            precio: nuevo precio unitario.
        """

        conexion = self.database.conectar()

        if conexion is None:
            return

        cursor = None

        try:
            cursor = conexion.cursor()

            # Verificar que la compra exista
            cursor.execute(
                "SELECT id FROM compra WHERE id = %s",
                (id_compra,)
            )

            if cursor.fetchone() is None:
                print("\nNo existe una compra con ese ID.")
                return

            sql = """
                UPDATE compra
                SET producto = %s,
                    cantidad = %s,
                    precio = %s
                WHERE id = %s
            """

            valores = (
                producto,
                cantidad,
                precio,
                id_compra
            )

            cursor.execute(sql, valores)

            conexion.commit()

            print("\n¡Compra actualizada correctamente!")

        except Exception as error:
            print("Error al actualizar la compra:", error)

        finally:
            if cursor:
                cursor.close()

            conexion.close()

    # ELIMINAR COMPRA
    def eliminar_compra(self, id_compra):
        """
        Elimina una compra de la base de datos mediante su ID.

        Args:
            id_compra: identificador de la compra que se eliminará.
        """

        conexion = self.database.conectar()

        if conexion is None:
            return

        cursor = None

        try:
            cursor = conexion.cursor()

            sql = """
                DELETE FROM compra
                WHERE id = %s
            """

            cursor.execute(sql, (id_compra,))

            if cursor.rowcount > 0:
                conexion.commit()
                print("\n¡Compra eliminada correctamente!")
            else:
                print("\nNo existe una compra con ese ID.")

        except Exception as error:
            print("Error al eliminar la compra:", error)

        finally:
            if cursor:
                cursor.close()

            conexion.close()