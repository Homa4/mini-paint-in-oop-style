import pygame

class MyTable:
    instance = None

    def __new__(cls):
        if MyTable.instance is None:
            MyTable.instance = super().__new__(cls)
        return MyTable.instance

    def __init__(self):
        self.screen = None
        self.acceleretor = []
        self.show_ghost_table = False
        self.ghost_table = None
        self.table_data = [["ID", "Start", "End"]]
        self.scroll_offset = 0
        
        
    def store_figure(self, element):
        self.table_data.append(element)
        print(self.table_data)
        
    def handle_events(self):
        if self.show_ghost_table:
            self.show_ghost_table = False
            # pygame.display.update((10, 400, 580, 190))
            self.screen.fill((255, 255, 255), self.ghost_table)
            print('action happens <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            return False
        else:
            self.show_ghost_table = True
            print('action happens >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            return True
    
    
    def add_element_in_table(self, element):
        self.table_data.append(element)
    
    def draw_table(self):
        if self.show_ghost_table:
            ROW_HEIGHT = 40
            VISIBLE_ROWS = 5  # Кількість видимих рядків у таблиці
            table_coord_x = 10
            table_coord_y = 400
            
            data = self.table_data
            scroll = self.scroll_offset
            table_width = 580
            col_widths = [int(table_width * 0.2), int(table_width * 0.4), int(table_width * 0.4)]
            
            # Ініціалізація кольорів
            WHITE = (255, 255, 255)
            BLACK = (0, 0, 0)
            GRAY = (200, 200, 200)
            
            # Ініціалізація шрифту
            font = pygame.font.Font(None, 36)
            
            # Малювання таблиці
            self.ghost_table = pygame.draw.rect(self.screen, 'grey', [table_coord_x, table_coord_y, table_width, ROW_HEIGHT * VISIBLE_ROWS])
            
            # Відображення видимих даних
            visible_data = data[scroll:scroll + VISIBLE_ROWS]
            for i, row in enumerate(visible_data):
                for j, cell in enumerate(row):
                    cell_x = table_coord_x + sum(col_widths[:j])
                    cell_y = table_coord_y + i * ROW_HEIGHT
                    cell_rect = pygame.Rect(cell_x, cell_y, col_widths[j], ROW_HEIGHT)
                    
                    # Заповнення комірки
                    pygame.draw.rect(self.screen, WHITE if i % 2 == 0 else GRAY, cell_rect)
                    pygame.draw.rect(self.screen, BLACK, cell_rect, 1)
                    
                    # Текст у комірці
                    text = font.render(str(cell), True, BLACK)
                    text_rect = text.get_rect(center=cell_rect.center)
                    self.screen.blit(text, text_rect)
     
    def handle_scroll(self, event):
        """Обробка скролу миші."""
        if self.show_ghost_table:
            # Оновлення зсуву
            self.scroll_offset -= event.y  # y: +1 (вверх), -1 (вниз)
            # Обмеження скролу в межах таблиці
            max_offset = max(0, len(self.table_data) - 5)  # 5 = VISIBLE_ROWS
            self.scroll_offset = max(0, min(self.scroll_offset, max_offset))
            # Оновлення відображення таблиці
            self.draw_table()
