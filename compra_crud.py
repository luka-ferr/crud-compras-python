from database import Database
from compra import Compra


class CompraCRUD:

    def __init__(self):
        self.database = Database()

    # REGISTRAR COMPRA
    def registrar_compra(self, compra):

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