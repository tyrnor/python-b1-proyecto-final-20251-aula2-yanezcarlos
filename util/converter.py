from abc import ABC, abstractmethod
from users.user import Cashier, Customer
from products.product import Hamburger, Soda, Drink, HappyMeal
from util.product_type import ProductType
import pandas as pd

# Write your code here


class Converter(ABC):
    @abstractmethod
    def convert(self, dataFrame: pd.DataFrame, *args) -> list:
        pass

    def print(self, objects):
        for item in objects:
            print(item.describe())


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
