import pygame
import sys

pygame.init()

# Налаштування екрану
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Таблиця зі скролом в Pygame")

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 150, 255)

# Шрифт
font = pygame.font.Font(None, 36)

# Початкові дані для таблиці
table_data = [["ID", "Назва", "Кількість"]]
next_id = 1

# Початковий зсув для скролу
scroll_offset = 0
ROW_HEIGHT = 40
VISIBLE_ROWS = 10  # Скільки рядків видно на екрані

# Функції для роботи з таблицею
def draw_table(screen, data, x, y, scroll, row_height=ROW_HEIGHT, col_widths=[100, 300, 150]):
    """Малює таблицю на екрані з урахуванням скролу."""
    visible_data = data[max(0, scroll):]
    for i, row in enumerate(visible_data[:VISIBLE_ROWS]):
        for j, cell in enumerate(row):
            cell_x = x + sum(col_widths[:j])
            cell_y = y + i * row_height
            cell_rect = pygame.Rect(cell_x, cell_y, col_widths[j], row_height)
            
            # Заповнення комірки
            pygame.draw.rect(screen, WHITE if (i + scroll) % 2 == 0 else GRAY, cell_rect)
            pygame.draw.rect(screen, BLACK, cell_rect, 1)
            
            # Текст у комірці
            text = font.render(str(cell), True, BLACK)
            text_rect = text.get_rect(center=cell_rect.center)
            screen.blit(text, text_rect)

def draw_button(screen, text, rect, color, text_color):
    """Малює кнопку."""
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
    button_text = font.render(text, True, text_color)
    text_rect = button_text.get_rect(center=rect.center)
    screen.blit(button_text, text_rect)

# Кнопка
button_rect = pygame.Rect(50, 500, 200, 50)

# Основний цикл
running = True
while running:
    screen.fill(WHITE)

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and button_rect.collidepoint(event.pos):
                # Додаємо новий елемент до таблиці
                table_data.append([next_id, f"Елемент {next_id}", next_id * 10])
                next_id += 1
            
            if event.button == 4:  # Прокрутка вверх
                scroll_offset = max(scroll_offset - 1, 0)
            if event.button == 5:  # Прокрутка вниз
                max_scroll = max(0, len(table_data) - VISIBLE_ROWS)
                scroll_offset = min(scroll_offset + 1, max_scroll)

    # Малюємо таблицю
    draw_table(screen, table_data, x=0, y=0, scroll=scroll_offset)

    # Малюємо кнопку
    draw_button(screen, "Додати елемент", button_rect, BLUE, WHITE)

    # Оновлюємо екран
    pygame.display.flip()

pygame.quit()
