from abc import ABC, abstractmethod

class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

class Device(Observable, ABC):
    def __init__(self):
        super().__init__()  
    
    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def is_on(self):
        pass
