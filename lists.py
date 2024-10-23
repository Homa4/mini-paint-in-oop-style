import pygame


class Lists:
    def __init__(self, field, screen):
        self.field = field
        self.screen = screen
        
    def menu(self):
        menu_height = (self.field*12)/100
        brash_block_size = round(menu_height/1.4)
        pygame.draw.rect(self.screen, 'gray', [0, 0, self.field, menu_height])
        pygame.draw.line(self.screen, 'black', (0,menu_height), (self.field, menu_height), 3)

        rectangale = pygame.draw.rect(self.screen, 'black', [10,10,brash_block_size,brash_block_size])
        pygame.draw.rect(self.screen, 'white', [15, 20, 40, 30])
        
        circle = pygame.draw.rect(self.screen, 'black', [70,10,brash_block_size,brash_block_size])
        pygame.draw.circle(self.screen, 'white', (95, 35), 20)
        pygame.draw.circle(self.screen, 'black', (95, 35), 18)

        
        point = pygame.draw.rect(self.screen, 'black', [130,10,brash_block_size,brash_block_size])
        pygame.draw.circle(self.screen, 'white', (155, 35), 10)
        
        line = pygame.draw.rect(self.screen, 'black', [190,10,brash_block_size,brash_block_size])
        pygame.draw.line(self.screen, 'white', (190, 10), (240, 60) , 3)
        
        shape_list = [rectangale, circle, point, line]
        shape_list_name = ['rectangle', 'circle', 'point', 'line']
        print(shape_list)
        
        red = pygame.draw.rect(self.screen, 'red', [self.field - 35, 22, 25, 25])
        blue = pygame.draw.rect(self.screen, 'blue', [self.field - 60, 22, 25, 25])
        green = pygame.draw.rect(self.screen, 'green', [self.field - 85, 22, 25, 25])
        
        rgb_colors = [red, blue, green]
        
        return shape_list, shape_list_name, rgb_colors, menu_height
              