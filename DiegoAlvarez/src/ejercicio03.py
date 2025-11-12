'''Args y kwargs'''

# Args: argumentos posicionales 

def procesar_dtos(*args) -> None:
    print(f"Argumentos posicionales recibidos: {args}")
    
mi_tup = (2, 3, 4)

procesar_dtos(mi_tup)

def saludo_dinamico(**kwargs) -> None:
    print(f"Argumentos nombrados recibidos: {kwargs}")
    
saludo_dinamico(nombre="Diego", edad=26)

# Generadores -> manjerar grndes volumenes de datos, utiliza la palabara yield en lugar de return

def generador_numeros(limite: int):
    """Generador que produce numeros hasta un limite dado"""
    print("Inicio de generador ")
    for num in range(limite):
        print(f"Bucle en prosicion {num}")
        yield num
    print("Fin del generador")

print("Uso de generador")
generador = generador_numeros(5+1)

for item in generador:
    print(f"Valor generado: {item}")
