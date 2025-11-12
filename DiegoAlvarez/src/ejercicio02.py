'''
    Funciones 
'''
    
def saludar(nombre: str = "Valeria") -> None:
    '''Funcion para saludar a una persona'''
    print(f"Hola {nombre}")
    
# Toma valor por defecto 
saludar()

# Toma valor dado en el llamado 
saludar("Diego")

'''Lambda'''

sumar =  lambda num1, num2 : num1 + num2

rersultado: int = sumar(5,7)

print(f"El resultado de la suma es: {rersultado}")

'''Maps'''

print(list(map(lambda num_1 : num_1 ** 2, range(5))))

def elevar_al_cuadrado(num_1: int) -> int:
    return num_1 ** 2

print(list(map(elevar_al_cuadrado, range(10))))

list_data = range(5)
cuadrado_lmbda = lambda x: x ** 2
map_filter = map(cuadrado_lmbda, list_data)

print(list(map_filter))

'''Filters'''
print("Filter")
print(list(filter(lambda x: x % 2 == 0, range(10))))