import pygame
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_text(screen, text, font, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def draw_chair_buttons(screen, center_x, center_y, radius, font, available_chairs):
    button_radius = 25
    angle_step = 360 / 12

    for i in range(12):
        angle = math.radians(i * angle_step)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        chair_num = i + 1
        chair_color = WHITE if chair_num in available_chairs else (200, 200, 200)

        pygame.draw.circle(screen, chair_color, (int(x), int(y)), button_radius)
        pygame.draw.circle(screen, BLACK, (int(x), int(y)), button_radius, 2)

        text = font.render(str(chair_num), True, BLACK)
        text_rect = text.get_rect(center=(int(x), int(y)))
        screen.blit(text, text_rect)
