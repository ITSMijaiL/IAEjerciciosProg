
#3.- Diseñe una clase que represente a un empleado con nombre, apellido, cédula,
#fecha de nacimiento y salario, y que permita obtener su nombre completo, sus
#iniciales, su edad y su ganancia anual.

from datetime import datetime

class Empleado:
    def __init__(self, nombre: str, apellidos: str, cedula: str, fecha_de_nacimiento: str, salario: float):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cedula = cedula
        self.fecha_de_nacimiento = datetime.strptime(fecha_de_nacimiento, "%d-%m-%Y")
        self.salario = salario
    def info(self):
        print(f"Nombre completo: {self.nombre} {self.apellidos}")
        print(f"Iniciales: {self.nombre[0]}.{self.apellidos[0]}.")
        print(f"Edad: {(datetime.now()).days-self.fecha_de_nacimiento//365} años")
        print(f"Ganancia anual: RD${self.salario*12}")

try:
    emp = Empleado(input("Nombres: "), 
               input("Apellidos: "),
               input("Cedula: "),
               input("Fecha de nacimiento: "),
               float(input("Salario: ")))
except TypeError:
    print("No se introdujo el salario bien")
emp.info()
