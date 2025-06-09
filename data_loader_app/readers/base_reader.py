from abc import ABC, abstractmethod

class BaseReader(ABC):
    def __init__(self, path):
        self._path = path

    @abstractmethod
    def leer_datos(self):
        pass