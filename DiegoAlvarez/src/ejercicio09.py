''' Modelado de objetos mediante composicion y herencia'''

class Motor:
    def __init__(self, tipo: str):
        self.tipo = tipo
        
class Rueda:
    def __init__(self, tamano: int):
        self.tamano = tamano
        
class Coche: 
    def __init__(self, marca: str, motor: Motor, ruedas: list[Rueda]):
        self.marca = marca
        self.motor = motor
        self.ruedas = ruedas
        
    def descripcion(self):
        print(f"Coche marca: {self.marca}")
        print(f"Tipo de motor: {self.motor.tipo}")
        print(f"Numero de ruedas: {len(self.ruedas)}")
        
auto_uno = Coche(
    marca="VW",
    motor=Motor("Diesel"),
    ruedas=[Rueda(16), Rueda(16), Rueda(16), Rueda(16)]
)

auto_uno.descripcion()