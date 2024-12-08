import pygame
from Shape import Shape


class RectShape(Shape):
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
            
            width = abs(temp_coords[0] - self.start_x)
            height = abs(temp_coords[1] - self.start_y)
            
            rect_x = min(self.start_x, temp_coords[0])
            rect_y = min(self.start_y, temp_coords[1])
            current_rect = (self.start_x, self.start_y, width, height)

            if self.prev_coords:
                pygame.draw.rect(self.screen, (255, 255, 255), self.prev_coords, 2)

            pygame.draw.rect(self.screen, (0, 0, 0), current_rect, 2)

            self.prev_coords = current_rect

    def draw(self, color, filled=True):
        if None not in (self.start_x, self.start_y, self.end_x, self.end_y):
            if self.start_y > 70 and self.end_y > 70: 
                width = abs(self.end_x - self.start_x)
                height = abs(self.end_y - self.start_y)
                rect_x = min(self.start_x, self.end_x)
                rect_y = min(self.start_y, self.end_y)

                if filled:
                    element = pygame.draw.rect(self.screen, color, (rect_x, rect_y, width, height))
                else:
                    element = pygame.draw.rect(self.screen, color, (rect_x, rect_y, width, height), 2)
                
# RectShape.update_elment(self, temp_coords)