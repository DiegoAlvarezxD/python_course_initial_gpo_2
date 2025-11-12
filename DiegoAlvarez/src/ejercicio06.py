import logging
from exception_custom.custom_exception import CustomError

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

logging.debug("Log nivel debug")

def function_con_error(n1: int):
    if(n1 < 0):
        raise CustomError("Error: numero menor a cero")
    logging.info("Eñ numero es correcto")
 
    
try: 
    function_con_error(-5)
except Exception as e:
    logging.info(f"Error: {e}")
else:
    logging.info(f"ejecucion correcta")
finally:
    logging.info("Ejecucion finalizada")