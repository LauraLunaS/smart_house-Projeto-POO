from device import Device
from transitions import Machine
from enum import Enum

class ThermostatStates(Enum):
    DESLIGADO = 'desligado'
    AQUECENDO = 'aquecendo'
    ESFRIANDO = 'esfriando'

class Thermostat(Device):
    _id_counter = 1

    def __init__(self):

        super().__init__()
        self.states = ThermostatStates
        self.machine = Machine(model=self, states=ThermostatStates, initial=ThermostatStates.DESLIGADO, after_state_change=self._notify_state_change)

        self.machine.add_transition(trigger='aquecer', source=ThermostatStates.DESLIGADO, dest=ThermostatStates.AQUECENDO)
        self.machine.add_transition(trigger='aquecer', source=ThermostatStates.ESFRIANDO, dest=ThermostatStates.AQUECENDO)

        self.machine.add_transition(trigger='esfriar', source=ThermostatStates.DESLIGADO, dest=ThermostatStates.ESFRIANDO)
        self.machine.add_transition(trigger='esfriar', source=ThermostatStates.AQUECENDO, dest=ThermostatStates.ESFRIANDO)

        self.machine.add_transition(trigger='desligar', source=ThermostatStates.AQUECENDO, dest=ThermostatStates.DESLIGADO)
        self.machine.add_transition(trigger='desligar', source=ThermostatStates.ESFRIANDO, dest=ThermostatStates.DESLIGADO)

        self.id = Thermostat._id_counter
        Thermostat._id_counter += 1

    def _notify_state_change(self):
        self.notify_observers(f'Termostato {self.id} está {self.state.value}')
        
    def status(self):
        return f"Termostato {self.id}. Estado atual: {self.state.value}"
    
    def is_on(self):
        return self.state != ThermostatStates.DESLIGADO
    

