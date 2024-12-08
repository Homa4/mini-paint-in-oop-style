import pygame
from PointShape import PointShape
from LineShape import LineShape

class DumbbellShape(PointShape, LineShape):
    def __init__(self, screen):
        super().__init__(screen)
        
    def detect_start(self, coords, color):
        LineShape.detect_start(self, coords)
        PointShape.detect_start(self, coords)
        PointShape.draw(self, color)
        

    def detect_end(self, coords):
        LineShape.detect_end(self, coords) 
        PointShape.detect_start(self, coords)
            
    def update_elment(self, temp_coords):
        LineShape.update_elment(self, temp_coords)  
            
    def draw(self, color):
        if self.start_x is not None and self.start_y is not None and self.end_y > 70:
            
            PointShape.draw(self, color)
            LineShape.draw(self, color)