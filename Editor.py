from abc import ABC, abstractmethod

class Editor(ABC):
    
    @abstractmethod
    def on_mouse_down():
        pass
    
    @abstractmethod
    def on_mouse_up():
        pass
    
    @abstractmethod
    def on_mouse_move():
        pass