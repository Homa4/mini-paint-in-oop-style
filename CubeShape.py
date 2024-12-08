import pygame
from RectShape import RectShape
from LineShape import LineShape


class CubeShape(RectShape, LineShape):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.prev_coords = None
        self.already_drawn = False

    def detect_start(self, coords):
        RectShape.detect_start(self, coords)
        LineShape.detect_start(self, coords)
        self.start_x, self.start_y = coords
        self.already_drawn = False


    def detect_end(self, coords):
        RectShape.detect_end(self, coords)
        LineShape.detect_end(self, coords)
        self.end_x, self.end_y = coords
        self.already_drawn = True

    def update_elment(self, temp_coords):
        if self.start_y is not None and self.start_y > 70:
            width = abs(temp_coords[0] - self.start_x)
            height = abs(temp_coords[1] - self.start_y)
            
            front = [self.start_x, self.start_y, width, height]
            back = [self.start_x+50, self.start_y+50, width, height]
            
            front_vertices = [
                (front[0], front[1]),  
                (front[0] + front[2], front[1]), 
                (front[0] + front[2], front[1] + front[3]),  
                (front[0], front[1] + front[3]), 
            ]
            back_vertices = [
                (back[0], back[1]),
                (back[0] + back[2], back[1]),
                (back[0] + back[2], back[1] + back[3]),
                (back[0], back[1] + back[3]),
            ]
            lines = [
                front_vertices,
                back_vertices
            ]

        
            current_cube = [
                (self.start_x, self.start_y, width, height), 
                (self.start_x + 50, self.start_y + 50, width, height), 
                # [front_vertices, back_vertices],
                lines
            ]

            if self.prev_coords:
                pygame.draw.rect(self.screen, (255, 255, 255), self.prev_coords[0], 2)
                pygame.draw.rect(self.screen, (255, 255, 255), self.prev_coords[1], 2)
                pygame.draw.line(self.screen, (255, 255, 255), self.prev_coords[2][0][0], self.prev_coords[2][1][0], 2)
                pygame.draw.line(self.screen, (255, 255, 255), self.prev_coords[2][0][1], self.prev_coords[2][1][1], 2)
                pygame.draw.line(self.screen, (255, 255, 255), self.prev_coords[2][0][2], self.prev_coords[2][1][2], 2)
                pygame.draw.line(self.screen, (255, 255, 255), self.prev_coords[2][0][3], self.prev_coords[2][1][3], 2)
                
                # self.clear_connection_lines(self.prev_coords[2][0], self.prev_coords[2][1])
                
                
            pygame.draw.rect(self.screen, (0, 0, 0), current_cube[0], 2)
            pygame.draw.rect(self.screen, (0, 0, 0), current_cube[1], 2)
            pygame.draw.line(self.screen, (0, 0, 0), current_cube[2][0][0], current_cube[2][1][0], 2)
            pygame.draw.line(self.screen, (0, 0, 0), current_cube[2][0][1], current_cube[2][1][1], 2)
            pygame.draw.line(self.screen, (0, 0, 0), current_cube[2][0][2], current_cube[2][1][2], 2)
            pygame.draw.line(self.screen, (0, 0, 0), current_cube[2][0][3], current_cube[2][1][3], 2)
            

            self.prev_coords = current_cube
        

        

    def draw_connection_lines(self, front, back):
        front_vertices = [
            (front[0], front[1]),  
            (front[0] + front[2], front[1]), 
            (front[0] + front[2], front[1] + front[3]),  
            (front[0], front[1] + front[3]), 
        ]
        back_vertices = [
            (back[0], back[1]),
            (back[0] + back[2], back[1]),
            (back[0] + back[2], back[1] + back[3]),
            (back[0], back[1] + back[3]),
        ]

        for front_point, back_point in zip(front_vertices, back_vertices):
            pygame.draw.line(self.screen, (0, 0, 0), front_point, back_point, 2)

    def clear_connection_lines(self, front, back):
        if not self.prev_coords:
            return

        front_vertices = [
            (front[0], front[1]),  
            (front[0] + front[2], front[1]), 
            (front[0] + front[2], front[1] + front[3]), 
            (front[0], front[1] + front[3]),  
        ]
        back_vertices = [
            (back[0], back[1]),
            (back[0] + back[2], back[1]),
            (back[0] + back[2], back[1] + back[3]),
            (back[0], back[1] + back[3]),
        ]

        for front_point, back_point in zip(front_vertices, back_vertices):
            pygame.draw.line(self.screen, (255, 255, 255), front_point, back_point, 2)


         
            
    def draw(self, color):
        if self.start_x is not None and self.start_y is not None and self.end_x is not None and self.end_y is not None:
             if self.start_y > 70 and self.end_y > 70: 
                self.already_drawn = True
                front_coords = [self.start_x, self.start_y, self.end_x, self.end_y]
                RectShape.detect_start(self, (front_coords[0], front_coords[1])) 
                RectShape.detect_end(self, (front_coords[2], front_coords[3]))
                RectShape.draw(self, color, False)
        
                offset = 50  
                back_coords = [front_coords[0] + offset, front_coords[1] + offset, front_coords[2] + offset, front_coords[3] + offset]
                RectShape.detect_start(self, (back_coords[0], back_coords[1]))
                RectShape.detect_end(self, (back_coords[2], back_coords[3]))
                RectShape.draw(self, color, False)

                front_vertices = [
                    (front_coords[0], front_coords[1]),  
                    (front_coords[2], front_coords[1]),  
                    (front_coords[2], front_coords[3]),  
                    (front_coords[0], front_coords[3]),  
                ]
                back_vertices = [
                    (back_coords[0], back_coords[1]),
                    (back_coords[2], back_coords[1]),
                    (back_coords[2], back_coords[3]),
                    (back_coords[0], back_coords[3]),
                ]

                for front, back in zip(front_vertices, back_vertices):
                    LineShape.detect_start(self, front)
                    LineShape.detect_end(self, back)
                    LineShape.draw(self, color)

        
