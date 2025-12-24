from abc import ABC, abstractmethod
from .food_package import FoodPackage, Wrapping, Bottle, Glass, Box

# Write your code here


# Clase abstracta que representa un producto genérico del sistema.
# Contiene los atributos comunes a todos los productos y define
# la interfaz que deben implementar las clases hijas.
class Product(ABC):
    def __init__(self, id: str, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def describe(self):
        """
        Devuelve una descripción completa del producto, incluyendo:
        - Tipo de producto
        - Nombre
        - Identificador
        - Precio
        - Información del empaquetado
        """
        return f"Product - Type: {self.type()}, Name: {self.name}, Id: {self.id} , Price: {self.price} , {self.foodPackage().describe()}."

    @abstractmethod
    def type(self) -> str:
        # Devuelve el tipo de producto.
        pass

    @abstractmethod
    def foodPackage(self) -> FoodPackage:
        # Devuelve el tipo de empaquetado del producto.
        pass


# Implementación concreta que representa un producto de tipo hamburguesa.
class Hamburger(Product):
    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)

    def type(self) -> str:
        return "Hamburger"

    def foodPackage(self) -> FoodPackage:
        return Wrapping()


# Implementación concreta que representa un producto de tipo refresco.
class Soda(Product):
    # Write your code here
    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)

    def type(self) -> str:
        return "Soda"

    def foodPackage(self) -> FoodPackage:
        return Bottle()


# Implementación concreta que representa una bebida.
class Drink(Product):
    # Write your code here
    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)

    def type(self) -> str:
        return "Drink"

    def foodPackage(self) -> FoodPackage:
        return Glass()


# Implementación concreta que representa un menú infantil.
class HappyMeal(Product):
    # Write your code here
    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)

    def type(self) -> str:
        return "Happy Meal"

    def foodPackage(self) -> FoodPackage:
        return Box()
