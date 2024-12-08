import pygame
pygame.init()


class Menu:
    def __init__(self, field, screen):
        self.field = field
        self.screen = screen
        self.currect_color = (255, 255, 255)
        
        
    def choose_color_for_detector(self, color):
        self.currect_color = color
        print("detector:", self.currect_color)
    
    def createMenu(self):
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
        
        dumbbell = pygame.draw.rect(self.screen, 'black', [250,10,brash_block_size,brash_block_size])
        pygame.draw.circle(self.screen, 'white', (265, 45), 8)
        pygame.draw.line(self.screen, 'white', (265, 45), (290, 25) , 3)
        pygame.draw.circle(self.screen, 'white', (290, 25), 8)
        
        cube = pygame.draw.rect(self.screen, 'black', [310,10,brash_block_size,brash_block_size])
        pygame.draw.rect(self.screen, 'white', [330, 20, 25, 25])
        pygame.draw.rect(self.screen, 'black', [332, 22, 20, 20])
        pygame.draw.line(self.screen, 'white', (330, 20), (315, 30), 3)
        pygame.draw.line(self.screen, 'white', (352, 20), (340, 30), 3)
        pygame.draw.line(self.screen, 'white', (352, 45), (340, 52), 3)
        pygame.draw.rect(self.screen, 'white', [315, 30, 25, 25])
        pygame.draw.rect(self.screen, 'black', [317, 32, 20, 20])
        
        
        
        shape_list = [rectangale, circle, point, line, dumbbell, cube]
        shape_list_name = ['rectangle', 'circle', 'point', 'line', 'dumbbell', 'cube']
        
        
        pygame.draw.circle(self.screen, self.currect_color, (400, 35), 30)
        pygame.draw.circle(self.screen, 'dark grey', (400, 35), 30, 3)


        
        table = pygame.draw.rect(self.screen, 'black', [440, 10,brash_block_size,brash_block_size])
        pygame.draw.rect(self.screen, 'white', [445, 17,brash_block_size-10, brash_block_size-15])
        pygame.draw.rect(self.screen, 'black', [446, 18,brash_block_size-13, brash_block_size-18])
        pygame.draw.line(self.screen, 'white', (445, 25), (485, 25), 3)
        pygame.draw.line(self.screen, 'white', (465, 17), (465, 50), 2)

        
        red = pygame.draw.rect(self.screen, 'red', [self.field - 35, 22, 25, 25])
        blue = pygame.draw.rect(self.screen, 'blue', [self.field - 60, 22, 25, 25])
        green = pygame.draw.rect(self.screen, 'green', [self.field - 85, 22, 25, 25])
        
        
        
        rgb_colors = [red, blue, green]
        
        return shape_list, shape_list_name, rgb_colors, table
    
