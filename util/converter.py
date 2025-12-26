from abc import ABC, abstractmethod
from users.user import Cashier, Customer
from products.product import Hamburger, Soda, Drink, HappyMeal
from util.product_type import ProductType
import pandas as pd

# Write your code here


class Converter(ABC):
    """
    Clase abstracta Converter. Define la interfaz común
    para todas las clases encargadas de convertir filas de un
    DataFrame en objetos.
    """

    @abstractmethod
    def convert(self, dataFrame: pd.DataFrame, *args) -> list:

        # Convierte las filas de un DataFrame en una lista de objetos.
        pass

    def print(self, objects):

        # Imprime por pantalla la descripción de cada objeto.
        for item in objects:
            print(item.describe())


# Clase encargada de convertir un DataFrame de cajeros en una lista de objetos Cashier.
class CashierConverter(Converter):
    def convert(self, dataFrame, *args) -> list:
        # Write your code here
        cashiers = []
        for _, row in dataFrame.iterrows():
            cashier = Cashier(
                dni=str(row["dni"]),
                name=row["name"],
                age=int(row["age"]),
                timeTable=row["timetable"],
                salary=float(row["salary"]),
            )
            cashiers.append(cashier)

        return cashiers


# Clase encargada de convertir un DataFrame de clientes en una lista de objetos Customer.
class CustomerConverter(Converter):
    # Write your code here
    def convert(self, dataFrame, *args) -> list:
        customers = []
        for _, row in dataFrame.iterrows():
            cashier = Customer(
                dni=str(row["dni"]),
                name=row["name"],
                age=int(row["age"]),
                email=row["email"],
                postalCode=str(row["postalcode"]),
            )
            customers.append(cashier)

        return customers


# Clase encargada de convertir un DataFrame de productos en una lista de objetos Product.
class ProductConverter(Converter):
    # Write your code here
    def convert(self, dataFrame, *args) -> list:
        products = []

        # Se espera que el primer argumento indique el tipo de producto, haciendo uso de la clase Enum ProductType
        product_type = args[0]

        for _, row in dataFrame.iterrows():
            if product_type == ProductType.HAMBURGER:
                product = Hamburger(
                    id=row["id"], name=row["name"], price=float(row["price"])
                )

            elif product_type == ProductType.SODA:
                product = Soda(
                    id=row["id"], name=row["name"], price=float(row["price"])
                )

            elif product_type == ProductType.DRINK:
                product = Drink(
                    id=row["id"], name=row["name"], price=float(row["price"])
                )

            elif product_type == ProductType.HAPPYMEAL:
                product = HappyMeal(
                    id=row["id"], name=row["name"], price=float(row["price"])
                )

            else:
                continue

            products.append(product)

        return products
