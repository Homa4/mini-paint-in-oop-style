import pygame
from RectEditor import RectEditor
from LineEditor import LineEditor
from CubeShape import CubeShape


class CubeEditor(RectEditor, LineEditor):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.cube_shape_sam = CubeShape(self.screen)
        self.temp_coord = None
        self.temp_coord_y = None
        self.drawing = None
    
    def on_mouse_down(self, event):
        self.cube_shape_sam.detect_start(event.pos)
        
    def on_mouse_up(self, event):
        self.cube_shape_sam.detect_end(event.pos)
    
    def start_dragging(self):
        self.drawing = True
    
    def stop_dragging(self):
        self.drawing = False
    
    def on_mouse_move(self, event):
        if event.pos[1] > 70 and self.drawing:
            x = event.pos[0]
            y = event.pos[1]
        
            xPdx = event.pos[0] + 50
            yPdx = event.pos[1] + 50
            self.cube_shape_sam.update_elment([x, y, xPdx, yPdx])
    
    def draw(self, color):
        self.cube_shape_sam.draw(color)