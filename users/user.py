from abc import ABC, abstractmethod


# Clase abstracta que representa un usuario genérico del sistema.
class User(ABC):
    def __init__(self, dni: str, name: str, age: int):
        self.dni = dni
        self.name = name
        self.age = age

    @abstractmethod
    def describe(self) -> str:

        # Devuelve una descripción textual del usuario.
        pass

# Clase concreta que representa a un cajero.
class Cashier(User):
    def __init__(self, dni: str, name: str, age: int, timeTable: str, salary: float):
        # Write your code here
        super().__init__(dni, name, age)
        self.timeTable = timeTable
        self.salary = salary

    def describe(self) -> str:
        
        # Devuelve una descripción del cajero con su información.
        return f"Cashier - Name: {self.name}, DNI: {self.dni} , Timetable: {self.timeTable}, Salary: {self.salary}."

# Clase concreta que representa un cliente.
class Customer(User):
    def __init__(self, dni: str, name: str, age: int, email: str, postalCode: str):
        # Write your code here
        super().__init__(dni, name, age)
        self.email = email
        self.postalCode = postalCode

    def describe(self) -> str:

        # Devuelve una descripción del cliente con su información personal.
        return f"Customer - Name: {self.name}, DNI: {self.dni} , Age: {self.age}, Email: {self.email}, Postal Code: {self.postalCode}"
