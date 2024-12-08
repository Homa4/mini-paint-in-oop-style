from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def detect_start():
        pass
    
    @abstractmethod
    def detect_end():
        pass
    
    @abstractmethod
    def draw():
        pass
    
    # @abstractmethod
    # def choosen_shape():
    #     pass