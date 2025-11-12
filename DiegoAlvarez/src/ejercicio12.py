class Notificador: 
    def enviar_mensaje(self, mensaje: str):
        return f"Hola {mensaje}"
    
    def cancelar(self, nuevo_mensaje: str):
        return f"Mensaje cancelado {nuevo_mensaje}"