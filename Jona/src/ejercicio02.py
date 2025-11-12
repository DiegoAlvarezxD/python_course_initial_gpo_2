'''
    Funciones
'''
    

def saludar(nombre: str = "Jona") -> None:
    ''' Función para saludar a una persona'''
    print(f"Hola, {nombre}")

# Toma el valor por defecto
saludar()

# Pasa un valor diferente
saludar("Jouse")



'''
    Lambdas
'''

sumar = lambda num_1, num_2: num_1 + num_2

resultado: int = sumar(5, 3)

print(f"El resultado de la suma es: {resultado}")

'''
    Maps
'''

print("Map")
def elevar_al_cuadrado(num_1: int) -> int:
    return num_1 ** 2

print(list(map(elevar_al_cuadrado, range(10))))

list_data: list = range(10)
cuadrado_lambda = lambda x: x ** 2
map_result = map(cuadrado_lambda, list_data)

print(list(map_result))


'''
    Filters
'''
print("Filter")
print(list(filter(lambda x: x % 2 == 0, range(10))))



# Asignación dinámica: Python infiere que 'precio_base' es un int.
precio_base = 100

# Tipado Opcional (Type Hinting): Mejor práctica para código profesional.
# No tiene efecto en tiempo de ejecución, pero ayuda a herramientas como MyPy.
tasa_iva: float = 0.21
nombre_producto: str = "Laptop"

# El tipado opcional en funciones documenta la intención
def calcular_total(precio: float, iva: float) -> float:
    """Calcula el precio final. Los hints hacen la firma clara."""
    return precio * (1 + iva)

# Llamada a la función
total = calcular_total(precio_base, tasa_iva)
print(f"El total a pagar por {nombre_producto} es: {total}")