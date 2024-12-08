from Shape import Shape
import pygame

class PointShape(Shape):
    def __init__(self, screen):
        self.screen = screen
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        
    def detect_start(self, coords):
        self.start_x = coords[0]
        self.start_y = coords[1]
            
    def detect_end(self, coords):
        self.end_x = coords[0]
        self.end_y = coords[1]
        
    def update_elment(self, temp_coords):
        pass
            
    def draw(self, color):
        if self.start_x is not None and self.start_y is not None:
            if self.start_y > 70 and self.end_y > 70:
                element = pygame.draw.circle(self.screen, color, (self.start_x, self.start_y), 10)
                return element
