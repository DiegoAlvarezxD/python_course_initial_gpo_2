class CustomError(Exception):
    ''' Clase de error personalizada '''
    pass


def funcion_con_error(n1: int):
    if(n1 < 0):
        raise CustomError("Ocurrió un error")
    print("El numero es correcto")



try:
    funcion_con_error(-5)
except Exception as e:
    print(f"Error: {e}")
else:
    print("Ejecución correcta")
finally:
    print("Ejecución finalizada")
    
    