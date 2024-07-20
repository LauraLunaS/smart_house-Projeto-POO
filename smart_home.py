from functools import reduce

class Home:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Home,cls).__new__(cls, *args, **kwargs)
        return cls.__instance


    def __init__(self):        
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.devices = []
        else:
            print('objeto já tem a variável initialized')

    def add_device(self, device):
        self.devices.append(device)
        print(f"Dispositivo {device.__class__.__name__} adicionado.")

    def list_devices(self):
        for idx, device in enumerate(self.devices):
            print(f"{idx}. {device.__class__.__name__}. {device.status()}")

    def states_all_devices(self):
        return [device.status for device in self.devices]
    
    def dispositivos_on(self):
        return list(filter(lambda device: device.is_on(), self.devices))
    
    def total_dispositivos_on(self):
        return reduce(lambda acc, device: acc + 1 if device.is_on() else acc, self.devices, 0)