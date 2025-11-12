
from dataclasses import dataclass
from typing import List


@dataclass
class Motor:
    tipo: str
    
@dataclass
class Rueda:
    tamano: int

@dataclass     
class Coche:
    marca: str
    motor: Motor
    ruedas: List[Rueda]
        
    def __str__(self):
        return (f"Coche marca: {self.marca}\n"
                f"Tipo de motor: {self.motor.tipo}\n"
                f"Número de ruedas: {len(self.ruedas)}")
        

auto_uno = Coche(
    marca="VW",
    motor=Motor("Diesel"),
    ruedas = [Rueda(2), Rueda(2)]
    )

#print(auto_uno)

coleccion: List[int] = ["Hola", 21, 2]

print(coleccion)