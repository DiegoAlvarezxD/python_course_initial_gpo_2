from src.ejercicio12 import Notificador


def test_enviar():
    notifica = Notificador()
    
    msj = notifica.enviar_mensaje("Diego")
    
    assert "Diego" in msj
    
    
def test_cancelar():
    notifica = Notificador()
    
    msj = notifica.cancelar("Diego1 Cancelado")
    
    assert "Diego" in msj