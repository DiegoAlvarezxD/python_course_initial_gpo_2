'''
    Decoradores -> Aumentar funcionalidad sin modificar la función original
'''
    
def decorador(func):
    def envoltura():
        print("Inicio")
        func()
        print("final")
    return envoltura
    

@decorador
def saludar():
    print("Hola, Mundo!")


# Decorador con args y kwargs
def decorador(func):
    def envoltura(*args, **kwargs):
        print(f"Inicio con args {args} y kwargs {kwargs}")
        func(*args, **kwargs)
        print("final de mi decorador")
    return envoltura


@decorador
def suma(n1: int, n2: int) -> None:
    print(f"La suma es: {n1 + n2}")
    
suma(5, 7)

#