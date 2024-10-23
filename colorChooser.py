import pygame
from Editor import Editor


class ColorChooser(Editor):
    def __init__(self, screen, rgb_colors):
        self.screen = screen
        self.rgb_colors = rgb_colors
        self.active_color = (255,255,255)
        
    def choose(self, event):
        for i in range(len(self.rgb_colors)):
            if self.rgb_colors[i].collidepoint(event.pos):
                self.active_color = self.screen.get_at(event.pos)
                return self.active_color
    def printElement():
        pass
        
    def calculateSize():
        pass