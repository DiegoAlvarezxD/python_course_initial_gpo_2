import time

''' Decoradores '''
def decora(func):
    def envoltura():
        print("Inicio")
        func()
        print("fin")
    return envoltura
   
   
@decora 
def saludar():
    print("Hola!!") 
    
saludar() 
def decorador(func):
    def envoltura(*args, **kwargs):
        print(f"Inicio con args {args} y kwargs {kwargs}")
        func(*args, **kwargs)
        print("final de mi decorador")
    return envoltura


@decorador
def suma(n1: int, n2: int) -> None:
    print(f"la suma es: {n1 + n2}")
    
suma(1,2)

def dec(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        print(f"Tiempo de inicio: {inicio}")
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de finalizacion: {fin}")
        print(f"Tiempo de ejecucion: {inicio - fin}")
        return resultado
    return envoltura

@dec
def tiempo_funcion():
    time.sleep(1)
    print("Acabamos!!")

tiempo_funcion()