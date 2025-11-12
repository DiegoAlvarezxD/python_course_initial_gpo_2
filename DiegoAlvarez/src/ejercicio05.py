class CustomError(Exception):
    '''clase error personalizada'''
    pass

def function_con_error(n1: int):
    if(n1 < 0):
        raise CustomError("Error: numero menor a cero")
    print("El numero es correcto")

try: 
    function_con_error(-5)
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"ejecucion correcta")
finally:
    print("Ejecucion finalizada")