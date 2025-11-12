

from DiegoAlvarez.src.ejercicio15 import Servicio
    
def test_servicio(mocker): 
    mock_logger = mocker.Mock()
    
    service = Servicio(mock_logger)
    
    service.procesar_data()
    
    mock_logger.info.assert_called_once_with("Procesando data...")