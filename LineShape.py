import pygame
from Shape import Shape

class LineShape(Shape):
    def __init__(self, screen):
        self.screen = screen
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.prev_coords = None  

    def detect_start(self, coords):
        self.start_x, self.start_y = coords
        self.prev_coords = None  

    def detect_end(self, coords):
        self.end_x, self.end_y = coords
        self.prev_coords = None  

    def update_elment(self, temp_coords):
        if self.start_y is not None and self.start_y > 70:
            
            if self.prev_coords:
                pygame.draw.line(self.screen, (255, 255, 255), (self.start_x, self.start_y), self.prev_coords, 2)
            
            pygame.draw.line(self.screen, (0, 0, 0), (self.start_x, self.start_y), temp_coords, 2)
            
            self.prev_coords = temp_coords

    def draw(self, color):
        if self.start_x is not None and self.start_y is not None and self.end_y > 70:
            
            pygame.draw.line(self.screen, color, (self.start_x, self.start_y), (self.end_x, self.end_y), 2)
