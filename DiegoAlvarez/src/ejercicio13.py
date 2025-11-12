from abc import ABC, abstractmethod

'''Inyeccion de dependencias'''

class ServiceEmail:
    def enviar_email(self, mensaje):
        print(f"Emial enviado - {mensaje}")


class Notificador: 
    def __init__(self, service: ServiceEmail):
        self.service = service
        
    def notificar(self, mensaje):
        self.service.enviar_email(mensaje)
        
        
service_email = ServiceEmail()
notifica = Notificador(service=service_email)

notifica.notificar("Contenido")


class MotorBase(ABC):
    @abstractmethod
    def encender(self):
        pass
    

class MotorElectronico(MotorBase):
    def encender(self):
        print("Encendido electrico")

class Motorgasolina(MotorBase):
    def encender(self):
        print("Encendido a gasolina")

class Auto:
    def __init__(self, motor_base: MotorBase):
        self.motor = motor_base
        
    def arrancar(self):
        self.motor.encender()
        
auto = Auto(MotorElectronico())
autoGas = Auto(Motorgasolina())

auto.arrancar( )
autoGas.arrancar()