from Editor import Editor
import pygame
from PointShape import PointShape

class PointEditor(Editor):
    def __init__(self, screen):
        self.screen = screen
        self.point_shape_sam = PointShape(self.screen)
    
    def on_mouse_down(self, event):
        self.point_shape_sam.detect_start(event.pos)
    
    def on_mouse_up(self, event):
        self.point_shape_sam.detect_end(event.pos)
        # self.line_shape_sam.draw() 
    
    def on_mouse_move(self, event):
        pass
    
    def start_dragging(self):
        pass
    
    def stop_dragging(self):
        pass
    
    def draw(self, color):
        self.point_shape_sam.draw(color)