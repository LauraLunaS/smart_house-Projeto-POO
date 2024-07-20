from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self, message: str):
        pass

class ConcreteObserver(Observer):

    def update(self, message: str):
        print(f"Notificação recebida: {message}")
