import pygame
from Editor import Editor

class Printer(Editor):
    def __init__(self, screen, shape_type, shape_coords, chosen_color, chosen_size):
        self.screen = screen
        self.shape_type = shape_type 
        self.shape_coords = shape_coords 
        self.chosen_color = chosen_color
        self.chosen_size = int(chosen_size) 

    def printElement(self):
        start, end = self.shape_coords
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        
        if start[1] < 70 or end[1] < 70:
            print("Drawing restricted in this area.")
            return

        if self.shape_type == 'rectangle':
            pygame.draw.rect(self.screen, self.chosen_color, [start[0], start[1], dx, dy], self.chosen_size)

        elif self.shape_type == 'circle':
            radius = int(((dx) ** 2 + (dy) ** 2) ** 0.5 / 2)
            center = (start[0] + dx // 2, start[1] + dy // 2)
            pygame.draw.circle(self.screen, self.chosen_color, center, radius, self.chosen_size)

        elif self.shape_type == 'point':
            pygame.draw.circle(self.screen, self.chosen_color, start, 10)
            
        elif self.shape_type == 'line':
            pygame.draw.line(self.screen, self.chosen_color, start, end, 4)
    
    def choose():
        pass
    
    def calculateSize():
        pass
