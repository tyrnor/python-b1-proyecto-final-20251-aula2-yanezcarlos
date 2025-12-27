"""
Ejercicio 1: Sistema de comida rápida

Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón.
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium"

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón.
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()

Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden.

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos.


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv:
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno
b.	Convertir clientes: Función creada por el alumno
c.	Convertir productos: Función creada por el alumno
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""

# Write your code here
from util.file_manager import CSVFileManager
from util.converter import CashierConverter, CustomerConverter, ProductConverter
from util.product_type import ProductType
from orders.order import Order
import pandas as pd
from datetime import datetime


# Clase principal encargada de coordinar el flujo completo del programa.
# Lee los archivos CSV, convierte los datos en objetos, interactua con
# el usuario y crea una orden de compra.
class PrepareOrder:
    # Write your code here

    def __init__(self) -> None:
        """
        Constructor de la clase PrepareOrder.
        Lee todos los archivos CSV y convierte los datos en
        listas de objetos.
        """
        # Leer todos los archivos CSV.
        df_cashiers = CSVFileManager("./data/cashiers.csv").read()
        df_customers = CSVFileManager("./data/customers.csv").read()
        df_drinks = CSVFileManager("./data/drinks.csv").read()
        df_hamburgers = CSVFileManager("./data/hamburgers.csv").read()
        df_happy_meals = CSVFileManager("./data/happyMeal.csv").read()
        df_sodas = CSVFileManager("./data/sodas.csv").read()

        # Convertir los DataFrames en listas de objetos.
        self.cashiers = CashierConverter().convert(df_cashiers)
        self.customers = CustomerConverter().convert(df_customers)

        product_converter = ProductConverter()
        self.products = []
        self.products += product_converter.convert(df_drinks, ProductType.DRINK)
        self.products += product_converter.convert(df_hamburgers, ProductType.HAMBURGER)
        self.products += product_converter.convert(
            df_happy_meals, ProductType.HAPPYMEAL
        )
        self.products += product_converter.convert(df_sodas, ProductType.SODA)

    def _find_cashier_by_dni(self, dni: str):
        """
        Busca un cajero por su DNI dentro de la lista de cajeros.
        Devuelve la instancia de Cashier si lo encuentra o None en
        caso contrario.
        """
        for cashier in self.cashiers:
            if cashier.dni == dni:
                return cashier
        return None

    def _find_customer_by_dni(self, dni: str):
        """
        Busca un cliente por su DNI dentro de la lista de clientes.
        Devuelve la instancia de Customer si lo encuentra o None en
        caso contrario.
        """
        for customer in self.customers:
            if customer.dni == dni:
                return customer
        return None

    def _find_product_by_id(self, id: str):
        """
        Busca un producto por su ID dentro de la lista de productos.
        Devuelve la instancia del producto si lo encuentra o None en
        caso contrario.
        """
        for product in self.products:
            if product.id == id:
                return product
        return None

    def _save_order(self, order: Order):
        """
        Guarda la información básica de una orden en un archivo CSV.
        Si el archivo ya existe, añade la nueva orden al final.
        """
        data = {
            "cashier_dni": [order.cashier.dni],
            "customer_dni": [order.customer.dni],
            "date_time": [datetime.now().strftime("%d/%m/%Y, %H:%M:%S")],
            "total": [order.calculateTotal()],
        }

        # Crear un DataFrame con la información de la orden.
        df = pd.DataFrame(data)

        manager = CSVFileManager("./data/orders.csv")

        try:
            # Si el archivo existe se leen los datos actuales.
            existing = manager.read()
            # Se añade la nueva orden al DataFrame existente.
            df = pd.concat([existing, df], ignore_index=True)
        except FileNotFoundError:
            # Si el archivo no existe se creará uno nuevo.
            pass

        # Guardar el DataFrame en el archivo CSV.
        manager.write(df)

    def run(self):
        """
        Método principal que ejecuta el flujo de la aplicación.
        Muestra la lista de cajeros y clientes, permite seleccionar productos,
        genera una orden, muestra el resultado final y permite guardar los datos
        en un archivo CSV.
        """

        # Mostrar lista de cajeros.
        print("Lista de cajeros")
        for cashier in self.cashiers:
            print(cashier.describe())

        cashier = None

        while cashier is None:
            dni_cashier = input("Introduce el DNI del cajero: ").strip()
            cashier = self._find_cashier_by_dni(dni_cashier)
            if cashier is None:
                print("DNI no encontrado. Inténtelo de nuevo.")

        print(f"\nCajero escogido: {cashier.describe()}")

        # Mostrar lista de clientes
        print("\nLista de clientes")
        for customer in self.customers:
            print(customer.describe())

        customer = None

        while customer is None:
            dni_customer = input("Introduce el DNI del cliente: ").strip()
            customer = self._find_customer_by_dni(dni_customer)
            if customer is None:
                print("DNI no encontrado. Intételo de nuevo.")

        print(f"\nCliente escogido: {customer.describe()}")

        # Crear la orden con el cajero y el cliente seleccionados.
        order = Order(cashier, customer)

        # Mostrar la lista de productos.
        print("\nLista de productos")
        for product in self.products:
            print(product.describe())

        con = True

        while con:
            product_id = input(
                "Introduce el ID del producto (o 'fin' para finalizar): "
            ).strip()
            if product_id.lower() == "fin":
                break

            product = self._find_product_by_id(product_id.upper())

            if product is None:
                print("ID de producto no encontrado. Inténtelo de nuevo.")
                continue

            # Añadir el producto a la orden.
            order.add(product)

            # Preguntar si se quieren añadir más productos
            while True:
                more = input("¿Quieres añadir otro producto? (si/no): ").strip().lower()
                if more == "si":
                    break
                elif more == "no":
                    con = False
                    break
                else:
                    print("Respuesta no válida. Escribe 'si' o 'no'.")

        # Mostrar el pedido final.
        print("\nPedido final")
        order.show()

        # Preguntar si se quiere guardar el pedido.
        save = input("¿Quieres guardar el pedido? (si/no): ").strip().lower()
        if save == "si":
            self._save_order(order)
            print("Pedido guardado correctamente.")


if __name__ == "__main__":
    app = PrepareOrder()
    app.run()
