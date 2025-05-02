import pygame
import math

# pygameの初期化を確実に行う
pygame.init()

# フォントの定義（pygameの初期化後）
FONT = pygame.font.SysFont('Arial', 24)

def draw_text(screen, text, font, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def draw_chair_buttons(screen, available_chairs, center_x, center_y, radius):
    button_radius = 25
    angle_step = 360 / 12

    for i in range(12):
        angle = math.radians(i * angle_step)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        chair_num = i + 1
        chair_color = (255, 255, 255) if chair_num in available_chairs else (200, 200, 200)

        pygame.draw.circle(screen, chair_color, (int(x), int(y)), button_radius)
        pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), button_radius, 2)

        text = FONT.render(str(chair_num), True, (0, 0, 0))
        text_rect = text.get_rect(center=(int(x), int(y)))
        screen.blit(text, text_rect)

def prompt_defender_choice(screen, message, font):
    draw_text(screen, message, font, (0, 0, 0), 20, 500)
