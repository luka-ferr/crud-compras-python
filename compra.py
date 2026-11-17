
class Compra:
    """
    Clase que representa una compra realizada.

    Atributos:
        id: identificador único de la compra.
        producto: nombre del producto.
        cantidad: unidades compradas.
        precio: precio unitario del producto.
    """

    def __init__(self, producto, cantidad, precio, id=None):
        """"
        Inicializa un objeto Compra con sus respectivos atributos.
        """
        self.id = id
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

    def calcular_total(self):
        """
        Calcula el valor total de la compra.

        Returns:
            float: resultado de multiplicar cantidad por precio.
        """
        return self.cantidad * self.precio
