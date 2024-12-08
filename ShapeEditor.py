import pygame
from Menu import Menu
from LineEditor import LineEditor
from PointEditor import PointEditor
from RectEditor import RectEditor
from ElipsEditor import ElipsEditor
from DumbbellEditor import DumbbellEditor
from CubeEditor import CubeEditor
from ShapeChooser import ShapeChooser
from MyTable import MyTable

class ShapeEditor:
    def __init__(self, field, screen, clock, table_sam):
        self.table_sam = table_sam
        self.field = field
        self.screen = screen
        self.clock = clock
        self.ghost_table_active = False
        self.project_running = True
    
    def code_runner(self):
        menu = Menu(self.field, self.screen)
        shape_list, shape_list_name, rgb_colors, table = menu.createMenu()
        line_editor = LineEditor(self.screen)
        point_editor = PointEditor(self.screen)
        rect_editor = RectEditor(self.screen)
        elips_editor = ElipsEditor(self.screen)
        shape_chooser = ShapeChooser(self.screen, shape_list, shape_list_name)
        dumbbell_editor = DumbbellEditor(self.screen)
        cube_editor = CubeEditor(self.screen)

        chosen_shape = None
        active_color = (0, 0, 0)  # Default color is black
        
        editor_list = {
            'point': point_editor,
            'line': line_editor,
            'rectangle': rect_editor,
            'circle': elips_editor,
            'dumbbell': dumbbell_editor,
            'cube': cube_editor,
        }
        
        settings_obj = {
            'shape': 'shape',
            'start': (0, 0),
            'end': (0, 0),
            'screen': self.screen,
            'color': active_color
        }
        
        while self.project_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.project_running = False
                
                menu.createMenu()
                
                if event.type == pygame.MOUSEWHEEL:
                    self.table_sam.handle_scroll(event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[1] < 70 and event.button == 1:
                        
                        if table.collidepoint(event.pos):
                            self.ghost_table_active = self.table_sam.handle_events()
                            self.table_sam.draw_table()
                            print('action happens =============================')
                                                    
                        
                        
                        
                        for color_rect in rgb_colors:
                            if color_rect.collidepoint(event.pos):
                                active_color = self.screen.get_at(event.pos)  
                                settings_obj['color'] = active_color
                                menu.choose_color_for_detector(active_color)
                                print(f"Selected color: {active_color}")
                                break
                        else:   
                            chosen_shape = shape_chooser.choose(event)
                            settings_obj['shape'] = chosen_shape
                            print(f"Chosen shape: {chosen_shape}")
                    
                    elif chosen_shape is not None:
                        if chosen_shape == 'dumbbell':
                            editor_list[chosen_shape].on_mouse_down(event, active_color)
                        else:
                            editor_list[chosen_shape].on_mouse_down(event)
                        
                        settings_obj['start'] = event.pos
                        editor_list[chosen_shape].start_dragging()
                
                if event.type == pygame.MOUSEMOTION and chosen_shape is not None:
                    editor_list[chosen_shape].on_mouse_move(event)
                
                if event.type == pygame.MOUSEBUTTONUP and chosen_shape is not None:
                    if event.button == 1:
                        editor_list[chosen_shape].stop_dragging()
                        editor_list[chosen_shape].on_mouse_up(event)
                        settings_obj['end'] = event.pos
                        editor_list[chosen_shape].draw(active_color)
                        
                        if event.pos[1] > 70:
                            self.table_sam.store_figure([
                             settings_obj['shape'], 
                             settings_obj['start'], 
                             settings_obj['end']])
                            
                            self.table_sam.draw_table()
                        
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
