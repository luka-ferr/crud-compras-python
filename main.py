
from database import conectar


# CREATE: Registrar una compra
def registrar_compra():
    conexion = conectar()

    if conexion is None:
        return

    try:
        producto = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio unitario: "))

        if cantidad <= 0 or precio <= 0:
            print("La cantidad y el precio deben ser mayores a cero.")
            return

        cursor = conexion.cursor()

        sql = """
            INSERT INTO compra
            (producto, cantidad, precio)
            VALUES (%s, %s, %s)
        """

        valores = (producto, cantidad, precio)

        cursor.execute(sql, valores)
        conexion.commit()

        print("Compra registrada correctamente")

    except ValueError:
        print("Error: ingresa valores numéricos válidos.")

    except Exception as error:
        print("Error al registrar:", error)

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()


if __name__ == "__main__":
    registrar_compra()
