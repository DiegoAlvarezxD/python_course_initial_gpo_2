''' Herencia y composicion'''

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print("hacer un sonido!!")
        
class Perro(Animal):
    def __init__(self, nombre="Perro"):
        super().__init__(nombre)
        
    def hablar(self):
        print(self.nombre)
        print("Guau Guau")

perro = Perro()

nombre_animal = perro.nombre