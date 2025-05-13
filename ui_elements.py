# ui_elements.py
import pygame

# タイトル描画
def draw_title(screen, font):
    title_text = font.render("電気椅子ゲーム", True, (0, 0, 0))
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 10))

# ルールプレート
def draw_rules_plate(screen, font):
    plate_x = 600
    plate_y = 100
    plate_width = 300
    plate_height = 180
    plate_color = (0, 0, 0)
    border_color = (255, 255, 255)
    text_color = (255, 255, 255)
    title_color = (255, 0, 0)

    # 背景と枠線
    pygame.draw.rect(screen, plate_color, (plate_x, plate_y, plate_width, plate_height))
    pygame.draw.rect(screen, border_color, (plate_x, plate_y, plate_width, plate_height), 2)

    # タイトルとルール文
    lines = [
        ("勝利条件", title_color),
        ("▼最終的なPで上回る", text_color),
        ("▼40Pを先取する", text_color),
        ("▼電流を3回食らわせる", text_color)
    ]
    for i, (text, color) in enumerate(lines):
        label = font.render(text, True, color)
        screen.blit(label, (plate_x + 10, plate_y + 10 + i * 30))

# テキスト描画
def draw_prompt(screen, prompt_text, font):
    draw_text(screen, prompt_text, font,  (0, 0, 0), 20, 500)

def draw_text(screen, text, font, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))
