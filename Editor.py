from abc import ABC,abstractmethod

class Editor(ABC):
    @abstractmethod
    def printElement():
        pass
    
    @abstractmethod
    def choose():
        pass
    
    @abstractmethod
    def calculateSize():
        pass