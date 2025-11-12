from abc import ABC, abstractmethod

'''
    Inyeccion de dependencias
'''

# Inyección por constructor
class ServiceEmailA:
    def enviar_email(self, mensaje):
        print(f"Email enviado - {mensaje}")

class NotificadorA:
    def __init__(self, service: ServiceEmailA):
        self.service = service
        
    def notificar(self, mensaje):
        self.service.enviar_email(mensaje)
        
service_email = ServiceEmailA()
notifica = NotificadorA(service=service_email)

notifica.notificar("Contenido constructor")


# Inyección por setter
class ServiceEmail:
    def enviar_email(self, mensaje):
        print(f"Email enviado - {mensaje}")

class Notificador:
    
    def set_email_service(self, service_email: ServiceEmail):
        self.service = service_email
        
    def notificar(self, mensaje):
        self.service.enviar_email(mensaje)
        
service_email = ServiceEmail()
notifica = Notificador()
notifica.set_email_service(service_email=service_email)
notifica.notificar("Contenido setter")


class MotorBase(ABC):
    @abstractmethod
    def encender(self):
        pass
    
class MotorElectrico(MotorBase):
    def encender(self):
        print("Encendido electrico")
        
class MotorGasolina(MotorBase):
    def encender(self):
        print("Encendido gasolina")


class Auto:
    def __init__(self, motor_base: MotorBase):
        self.motor = motor_base
        
    def arrancar(self):
        self.motor.encender()
        
auto_electrico = Auto(MotorElectrico())
auto_gas = Auto(MotorGasolina())

auto_electrico.arrancar()
auto_gas.arrancar()