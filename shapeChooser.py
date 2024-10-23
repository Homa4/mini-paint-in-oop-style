import pygame
from Editor import Editor

class ShapeChooser(Editor):
    def __init__(self, screen, shape_list, shape_list_name):
        self.screen = screen
        self.shape_list = shape_list
        self.shape_list_name = shape_list_name
        self.active_shape = 0
        
    def choose(self, event):
        for i in range(len(self.shape_list)):
            if self.shape_list[i].collidepoint(event.pos):
                self.active_shape = self.screen.get_at(event.pos)
                return self.shape_list_name[i]
            
    def printElement():
        pass
        
    def calculateSize():
        pass