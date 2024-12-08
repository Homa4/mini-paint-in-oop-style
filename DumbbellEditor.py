import pygame
from PointEditor import PointEditor
from LineEditor import LineEditor
from DumbbellShape import DumbbellShape

class DumbbellEditor(PointEditor, LineEditor):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.dumbbell_shape_sam = DumbbellShape(self.screen)
        
    def on_mouse_down(self, event, color):
        self.dumbbell_shape_sam.detect_start(event.pos, color)
    
    def on_mouse_up(self, event):
        self.dumbbell_shape_sam.detect_end(event.pos)
    
    def start_dragging(self):
        self.drawing = True
    
    def stop_dragging(self):
        self.drawing = False
    
    def on_mouse_move(self, event):
        if event.pos[1] > 70 and self.drawing:
            self.temp_coord = self.dumbbell_shape_sam.update_elment((event.pos))
    
    def draw(self, color):
        self.dumbbell_shape_sam.draw(color)