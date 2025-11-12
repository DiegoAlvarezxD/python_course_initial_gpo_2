from src.ejercicio11 import Notificador


def test_enviar():
    notifica = Notificador()
    
    msj = notifica.envia_mensaje("Jona")
    
    assert "Jona" in msj