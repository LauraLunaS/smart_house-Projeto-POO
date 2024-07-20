from device import Device
from transitions import Machine
from enum import Enum

class LightStates(Enum):
    DESLIGADA = 'desligada'
    LIGADA = 'ligada'


class Light(Device):  
    _id_counter = 1

    def __init__(self):
        super().__init__()
        self.states = LightStates
        self.machine = Machine(model=self, states=LightStates, initial=LightStates.DESLIGADA, after_state_change=self._notify_state_change)

        self.machine.add_transition(trigger='ligar', source=LightStates.DESLIGADA, dest=LightStates.LIGADA)
        self.machine.add_transition(trigger='desligar', source=LightStates.LIGADA, dest=LightStates.DESLIGADA)

        self.id = Light._id_counter
        Light._id_counter += 1

    def _notify_state_change(self):
        self.notify_observers(f'Luz {self.id} foi {self.state.value}')

    def status(self):
        return f'Luz {self.id}. Estado atual: {self.state.value}'
    
    def is_on(self):
        return self.state == LightStates.LIGADA