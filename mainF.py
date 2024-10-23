import pygame
from lists import Lists
from pointDraw import PointDraw
from colorChooser import ColorChooser
from shapeChooser import ShapeChooser
from sizeChooser import SizeChooser
from printer import Printer
# from gumTrail import RubberBand
# from pointDraw import PointDraw

pygame.init()

field = 600
screen = pygame.display.set_mode((field, field))
clock = pygame.time.Clock()
pygame.display.set_caption('Paint_copy')

class Main():
    def __init__(self):
        pass

    def codeRunner(self, field, clock, screen):
        screen.fill('white')
        
        project_running = True
        editor_sample = Lists(field, screen)  
        shape_list, shape_list_name, rgb_colors, menu_height = editor_sample.menu()

        # point_draw_sample = PointDraw(screen, shape_list, rgb_colors, menu_height) 
        color_chooser_sample = ColorChooser(screen, rgb_colors)
        shape_chooser_sample = ShapeChooser(screen, shape_list, shape_list_name)
        # rubberBand = RubberBand(screen)
        size_chooser_sample = SizeChooser(screen)

        chosen_shape = None
        chosen_color = (0, 0, 0)  
        chosen_size = 1        
        dragging = False
        start_pos = None
        end_pos = None

        while project_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    project_running = False

                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    new_color = color_chooser_sample.choose(event)
                    if new_color:
                        chosen_color = new_color
                        # print(f"Chosen Color: {chosen_color}")

        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    new_shape = shape_chooser_sample.choose(event)
                    if new_shape:
                        chosen_shape = new_shape
                        # print(f"Chosen Shape: {chosen_shape}")
                # print(event)
                chosen_size = size_chooser_sample.handleEvent(event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    start_pos = event.pos

                    dragging = True

                if event.type == pygame.MOUSEMOTION and dragging:
                    end_pos = event.pos

                if event.type == pygame.MOUSEBUTTONUP and dragging:
                    end_pos = event.pos
                    dragging = False
                    if chosen_shape and start_pos and end_pos:
                        printer = Printer(screen, chosen_shape, (start_pos, end_pos), chosen_color, chosen_size)
                        printer.printElement()
                        
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()


main = Main()

main.codeRunner(field, clock, screen)
