from device import Device
from transitions import Machine
from enum import Enum

class SecuritySistemStates(Enum):
    DESARMADO = 'desarmado'
    ARMADO_COM_GENTE_EM_CASA = 'armado com gente em casa'
    ARMADO_SEM_NINGUEM_EM_CASA = 'armado sem gente em casa'

class SecuritySystem(Device):
    _id_counter = 1

    def __init__(self):
        super().__init__()
        self.states = SecuritySistemStates
        self.machine = Machine(model=self, states=SecuritySistemStates, initial=SecuritySistemStates.DESARMADO, after_state_change=self._notify_state_change)

        self.machine.add_transition(trigger='armar_com_gente_em_casa', source=SecuritySistemStates.DESARMADO, dest=SecuritySistemStates.ARMADO_COM_GENTE_EM_CASA)
        self.machine.add_transition(trigger='armar_com_gente_em_casa', source=SecuritySistemStates.ARMADO_SEM_NINGUEM_EM_CASA, dest=SecuritySistemStates.ARMADO_COM_GENTE_EM_CASA)

        self.machine.add_transition(trigger='armar_sem,_gente_em_casa', source=SecuritySistemStates.DESARMADO, dest=SecuritySistemStates.ARMADO_SEM_NINGUEM_EM_CASA)
        self.machine.add_transition(trigger='armar_sem_gente_em_casa', source=SecuritySistemStates.ARMADO_COM_GENTE_EM_CASA, dest=SecuritySistemStates.ARMADO_SEM_NINGUEM_EM_CASA)

        self.machine.add_transition(trigger='desarmar', source=SecuritySistemStates.ARMADO_COM_GENTE_EM_CASA, dest=SecuritySistemStates.DESARMADO)
        self.machine.add_transition(trigger='desarmar', source=SecuritySistemStates.ARMADO_SEM_NINGUEM_EM_CASA, dest=SecuritySistemStates.DESARMADO)

        self.id = SecuritySystem._id_counter
        SecuritySystem._id_counter += 1

    def _notify_state_change(self):
        self.notify_observers(f'Sistema de segurança {self.id} está {self.state.value}')

    def status(self):
        return f'Sistema de Segurança {self.id}. Estado atual: {self.state.value}'
    
    def is_on(self):
        return self.state != SecuritySistemStates.DESARMADO