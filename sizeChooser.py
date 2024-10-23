import pygame
import math
from Editor import Editor


class SizeChooser(Editor):
    def __init__(self, screen):
        self.screen = screen
        self.start_pos = None  
        self.end_pos = None  
        self.drawing = False   

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.start_pos = event.pos
            self.drawing = True

        elif event.type == pygame.MOUSEMOTION and self.drawing:
            self.end_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and self.drawing:
            self.end_pos = event.pos
            self.drawing = False
            return self.calculateSize() 

        return None

    def calculateSize(self):
        if self.start_pos and self.end_pos:
            dx = self.end_pos[0] - self.start_pos[0]
            dy = self.end_pos[1] - self.start_pos[1]
            size = int(math.sqrt(dx ** 2 + dy ** 2))
            return size
        return 1 
     
    def printElement():
        pass
    
    def choose():
        pass


