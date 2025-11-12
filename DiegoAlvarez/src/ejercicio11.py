''' Modelado de objetos mediante composicion y herencia'''
from dataclasses import dataclass

@dataclass
class Motor:
        tipo: str

@dataclass       
class Rueda:
    tamano: int
    
@dataclass        
class Coche: 
        marca: str
        motor: str
        ruedas: list
        
        def __str__(self):
            return (f"Coche marca: {self.marca}\n"
                    f"Tipo de motor: {self.motor.tipo}\n"
                    f"Numero de ruedas: {len(self.ruedas)}")
        
        
auto_uno = Coche(
    marca="VW",
    motor=Motor("Diesel"),
    ruedas=[Rueda(16), Rueda(16), Rueda(16), Rueda(16)]
)

print(auto_uno)