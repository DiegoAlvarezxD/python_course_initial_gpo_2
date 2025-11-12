import logging

from Jona.src.exceptions.exception_custom import CustomError


'''
    logging.debug("Log nivel debug")
    logging.info("Log nivel info")
    logging.warning("Log nivel warning")
    logging.error("Log nivel error")
'''
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)


def funcion_con_error(n1: int):
    if(n1 < 0):
        raise CustomError("Ocurrió un error")
    logging.info("El numero es correcto")



try:
    funcion_con_error(-5)
except Exception as e:
    logging.error(f"Error: {e}")
else:
    logging.info("Ejecución correcta")
finally:
    logging.info("Ejecución finalizada")
    