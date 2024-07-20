from abc import ABC, abstractmethod
from light import Light
from thermostat import Thermostat
from security_system import SecuritySystem

class DispositivoFactory:

    @staticmethod
    def create_device(tipo):
        if tipo == 'Luz':
            return Light()
        elif tipo == 'Termostato':
            return Thermostat()
        elif tipo == 'SistemaSeguranca':
            return SecuritySystem()
        else:
            raise ValueError(f"Tipo de dispositivo desconhecido: {tipo}")