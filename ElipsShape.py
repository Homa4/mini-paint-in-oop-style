from Shape import Shape
import pygame

class ElipsShape(Shape):
    def __init__(self, screen):
        self.screen = screen
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.prev_ellipse_rect = None  # Зберігаємо попередній еліпс для стирання

    def detect_start(self, coords):
        self.start_x, self.start_y = coords
        self.prev_ellipse_rect = None  # Скидаємо попередній еліпс при новому старті

    def detect_end(self, coords):
        self.end_x, self.end_y = coords
        self.prev_ellipse_rect = None  # Скидаємо попередній еліпс при завершенні

    def update_elment(self, temp_coords):
        if self.start_y is not None and self.start_y > 70:
            # Вираховуємо ширину і висоту тимчасового еліпса
            width = abs(temp_coords[0] - self.start_x)
            height = abs(temp_coords[1] - self.start_y)
            ellipse_x = min(self.start_x, temp_coords[0])
            ellipse_y = min(self.start_y, temp_coords[1])
            current_ellipse_rect = (ellipse_x, ellipse_y, width, height)

            # Стерти попередній тимчасовий еліпс, якщо він існує
            if self.prev_ellipse_rect:
                pygame.draw.ellipse(self.screen, (255, 255, 255), self.prev_ellipse_rect, 2)

            # Намалювати новий тимчасовий еліпс чорним кольором
            pygame.draw.ellipse(self.screen, (0, 0, 0), current_ellipse_rect, 2)

            # Оновити координати попереднього тимчасового еліпса
            self.prev_ellipse_rect = current_ellipse_rect

    def draw(self, color, filled=True):
        if None not in (self.start_x, self.start_y, self.end_x, self.end_y):
            if self.start_y > 70 and self.end_y > 70:
                width = abs(self.end_x - self.start_x)
                height = abs(self.end_y - self.start_y)
                ellipse_x = min(self.start_x, self.end_x)
                ellipse_y = min(self.start_y, self.end_y)

                if filled:
                    element = pygame.draw.ellipse(self.screen, color, (ellipse_x, ellipse_y, width, height))
                else:
                    element = pygame.draw.ellipse(self.screen, color, (ellipse_x, ellipse_y, width, height), 2)
                
                return element

