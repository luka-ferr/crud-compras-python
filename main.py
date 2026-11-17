
from compra import Compra
from compra_crud import CompraCRUD


class Aplicacion:
    """
    Clase principal encargada de controlar la aplicación.

    Gestiona el menú, la entrada de datos, las validaciones
    y la ejecución de las operaciones CRUD.
    """

    def __init__(self):
        self.crud = CompraCRUD()

    # MÉTODOS AUXILIARES

    def mostrar_menu(self):
        print("\n========== CRUD DE COMPRAS ==========")
        print("1. Registrar compra")
        print("2. Consultar compras")
        print("3. Actualizar compra")
        print("4. Eliminar compra")
        print("5. Salir")
        print("=====================================")

    def solicitar_entero(self, mensaje):
        while True:
            try:
                valor = int(input(mensaje))

                if valor <= 0:
                    print("El valor debe ser mayor que cero.")
                    continue

                return valor

            except ValueError:
                print("Error: ingresa un número entero válido.")

    def solicitar_decimal(self, mensaje):
        while True:
            try:
                valor = float(input(mensaje))

                if valor <= 0:
                    print("El valor debe ser mayor que cero.")
                    continue

                return valor

            except ValueError:
                print("Error: ingresa un número válido.")

    def solicitar_producto(self):
        while True:
            producto = input("Nombre del producto: ").strip()

            if producto:
                return producto

            print("El nombre del producto no puede estar vacío.")

    def formato_pesos(self, valor):
        return "$ {:,.0f}".format(valor).replace(",", ".")


    # OPERACIONES DEL CRUD

    def registrar(self):
        print("\n--- REGISTRAR COMPRA ---")

        producto = self.solicitar_producto()
        cantidad = self.solicitar_entero("Cantidad: ")
        precio = self.solicitar_decimal("Precio unitario: ")

        compra = Compra(producto, cantidad, precio)

        self.crud.registrar_compra(compra)

    def consultar(self):
        print("\n--- LISTA DE COMPRAS ---")

        compras = self.crud.consultar_compras()

        if not compras:
            print("No hay compras registradas.")
            return

        for compra in compras:
            print("--------------------------------")
            print(f"ID: {compra.id}")
            print(f"Producto: {compra.producto}")
            print(f"Cantidad: {compra.cantidad}")
            print(f"Precio: {self.formato_pesos(compra.precio)}")
            print(f"Total: {self.formato_pesos(compra.calcular_total())}")

        print("--------------------------------")

    def actualizar(self):
        print("\n--- ACTUALIZAR COMPRA ---")

        id_compra = self.solicitar_entero("ID de la compra: ")
        producto = self.solicitar_producto()
        cantidad = self.solicitar_entero("Nueva cantidad: ")
        precio = self.solicitar_decimal("Nuevo precio unitario: ")

        self.crud.actualizar_compra(
            id_compra,
            producto,
            cantidad,
            precio
        )

    def eliminar(self):
        print("\n--- ELIMINAR COMPRA ---")

        id_compra = self.solicitar_entero("ID de la compra: ")

        confirmacion = input(
            "¿Está seguro de eliminar esta compra? (s/n): "
        ).strip().lower()

        if confirmacion == "s":
            self.crud.eliminar_compra(id_compra)
        else:
            print("Operación cancelada.")


    # CONTROL PRINCIPAL

    def ejecutar(self):

        while True:
            self.mostrar_menu()

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.registrar()

            elif opcion == "2":
                self.consultar()

            elif opcion == "3":
                self.actualizar()

            elif opcion == "4":
                self.eliminar()

            elif opcion == "5":
                print("¡Gracias por utilizar el sistema!")
                break

            else:
                print("Opción no válida.")


if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.ejecutar()
