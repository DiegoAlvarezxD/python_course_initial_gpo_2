# Comentaario en Linea

'''
Comentarios multi lineas, puede ser con " o con '
'''
# Tipo de datos 

mi_variable = 10
print(type(mi_variable))

mi_variable_flotante = 10.5
print(type(mi_variable_flotante))

mi_variable_cadena = "Hola, Mundo"
print(type(mi_variable_cadena))

mi_variable_booleana = True
print(type(mi_variable_booleana))

print("Hola, Mundo")

# Listas
mi_lista: list = [1, 2, 3]
print("Mi lista antes de la modificacion: ", mi_lista)
mi_lista[2] = 4
print("Mi lista despues de la modificacion: ",mi_lista)

print(type(mi_lista))

# Tuplas
mi_tupla: tuple = (1, 2, 3)
#mi_tupla[2] = 5
print(type(mi_tupla))

# Diccionarios 
mi_diccionario: dict = {"Clave1": "Valor1", "clave2": "Valor2"}

# Sets
mi_set: set = {1, 2, 3}

# F-string
nombre: str = "Diego"

print("Hola, "+ nombre) # Concatenacion tradicional 

print(f"Hola, {nombre} esto es f string") # Concatenacion f string



'''
    Compresiones
'''

cuadrado: list = [x**2 for x in range(10)]

print(cuadrado)

# break y continue y else en bucles 
