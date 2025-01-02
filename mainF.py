import pygame
from ShapeEditor import ShapeEditor
from MyTable import MyTable


field = 600
screen = pygame.display.set_mode((field, field))
clock = pygame.time.Clock()
pygame.display.set_caption('copy_of_paint')
screen.fill('white')
table_sam = MyTable()
table_sam.screen = screen

print('table_sam->1', table_sam)
table_sam2 = MyTable()
print('table_sam->2', table_sam2)

shape_editor = ShapeEditor(field, screen, clock, table_sam)

shape_editor.code_runner()


