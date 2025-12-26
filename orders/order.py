from users import Cashier, Customer
from products.product import Product


# Clase que representa una orden de compra.
# Contiene la información del cajero, del cliente y los productos añadidos.
class Order:
    def __init__(self, cashier: Cashier, customer: Customer):
        self.cashier = cashier
        self.customer = customer
        self.products = []

    def add(self, product: Product):
        # Write your code here
        # Añade un producto a la orden.
        self.products.append(product)

    def calculateTotal(self) -> float:
        # Write your code here
        """
        Calcula el precio total de la orden sumando el precio
        de todos los productos añadidos.
        Devuelve el total redondeando a dos decimales.
        """
        total = 0.0

        for product in self.products:
            total += product.price

        return round(total, 2)

    def show(self):
        """
        Muestra por pantalla la información completa de la orden:
        - Datos del cliente
        - Datos del cajero
        - Lista de productos añadidos
        - Precio total de la orden
        """
        print("Hello : " + self.customer.describe())
        print("Was attended by : " + self.cashier.describe())
        for product in self.products:
            print(product.describe())
        print(f"Total price : {self.calculateTotal()}")
