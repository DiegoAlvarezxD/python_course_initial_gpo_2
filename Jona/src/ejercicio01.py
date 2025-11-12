# Comentario en linea


'''
Comentario de bloque
Que puede ser multilinea
Comilla simple
'''

# Tipos de dato

mi_variable: int = 10
print(type(mi_variable))

mi_variable: float = 10.5
print(type(mi_variable))

mi_variable: str = "Hola, Mundo"
print(type(mi_variable))

mi_variable: bool = True
print(type(mi_variable))

# Estructuras de datos
# Listas

mi_lista: list = [1, 2, 3]

print("Mi lista antes de la modificacion:", mi_lista)
mi_lista[2] = 4  # Modificando un elemento de la lista
print("Mi lista despues de la modificacion:", mi_lista)

print(type(mi_lista))

# Tuplas

mi_tupla: tuple = (1, 2, 3)

print(type(mi_tupla))

# Diccionarios
mi_diccionario: dict = {"clave1": "valor1", "clave2": "valor2"}

# Sets
mi_set: set = {1, 2, 3}

# f-strings
nombre: str = "Jona"

print("Hola, " + nombre)  # Concatenacion tradicional

print(f"Hola, {nombre}")  # Usando f-string


'''
    Compresiones
'''
cuadrados: list = [x**2 for x in range(10)]

print(cuadrados)

# Break y Continue y else en bucles

