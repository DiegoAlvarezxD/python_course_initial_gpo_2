class Procesador: 
    def __init__(self, marca: str, nucleos: int):
        self.marca = marca
        self.nucleos = nucleos

class Memoria:
    def __init__(self, tamano: int, velocidad: float):
        self. tamano = tamano
        self.velocidad = velocidad


class Computadora: 
    def __init__(self, procesador: Procesador, memoria: Memoria):
        self.procesador = procesador
        self.memoria = memoria
        
        def descripcion(self):
            print(f"Marca de procesador: {self.marca}")
            print(f"Nucleos de procesador: {self.nucleos}")
            print(f"Tamaño de la memoria: {self.tamano} MB")
            print(f"Velocidad del la memoria: {self.velocidad} MHz")


procesador = Procesador("Intel", 8)
memoria = Memoria(1024, 1000)


computadora = Computadora(procesador, memoria)


computadora.descripcion()