from Editor import Editor
import pygame
from ElipsShape import ElipsShape

class ElipsEditor(Editor):
    def __init__(self, screen):
        self.screen = screen
        self.elips_shape_sam = ElipsShape(self.screen)
        self.temp_coord = None
        self.drawing = None
    
    def on_mouse_down(self, event):
        self.elips_shape_sam.detect_start(event.pos)
    
    def on_mouse_up(self, event):
        self.elips_shape_sam.detect_end(event.pos)
        
    def start_dragging(self):
        self.drawing = True
    
    def stop_dragging(self):
        self.drawing = False
    
    def on_mouse_move(self, event):
        if event.pos[1] > 70 and self.drawing:
            self.temp_coord = self.elips_shape_sam.update_elment((event.pos))
    
    def draw(self, color):
        self.elips_shape_sam.draw(color)