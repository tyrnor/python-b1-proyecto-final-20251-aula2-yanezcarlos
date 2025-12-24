# Write your code here
from abc import ABC, abstractmethod


# Clase base abstracta que representa un paquete de comida genérico.
# Define la interfaz que deben implementar todos los tipos de empaquetado.
class FoodPackage(ABC):
    @abstractmethod
    def pack(self) -> str:

        # Devuelve el tipo de empaquetado utilizado para el producto.
        pass

    @abstractmethod
    def material(self) -> str:

        # Devuelve el material del empaquetado.
        pass

    def describe(self):

        # Devuelve una decripción del empaquetado combinando el tipo de paquete y el material.
        return f"Empaque: {self.pack()} , Material: {self.material()}"


# Implementación concreta de FoodPackage para productos envueltos.
class Wrapping(FoodPackage):
    # Write your code here
    def pack(self) -> str:
        return "Food Wrap Paper"

    def material(self) -> str:
        return "Aluminium"


# Implementación concreta de FoodPackage para bebidas embotelladas.
class Bottle(FoodPackage):
    # Write your code here
    def pack(self) -> str:
        return "Bottle"

    def material(self) -> str:
        return "Plastic"


# Implementación concreta de FoodPackage para bebidas servidas en vaso.
class Glass(FoodPackage):
    # Write your code here
    def pack(self) -> str:
        return "Glass"

    def material(self) -> str:
        return "Cardboard"


# Implementación concreta de FoodPackage para productos empaquetados en una caja.
class Box(FoodPackage):
    # Write your code here
    def pack(self) -> str:
        return "Box"

    def material(self) -> str:
        return "Cardboard"
