
class Compra:

    def __init__(self, producto, cantidad, precio, id=None):
        self.id = id
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

    def calcular_total(self):
        return self.cantidad * self.precio
