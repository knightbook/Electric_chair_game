# chair_buttons.py
# 最終チェック済み ✅
# このモジュールは、ゲーム画面上に配置された「椅子ボタン（1〜12）」の描画処理を担う。
# 各椅子は円周上に配置され、使用可否や椅子番号が視覚的に表示される。

import pygame
import math

# pygame初期化（フォント描画などに必要）
pygame.init()

# フォントの設定（椅子番号に使用）
FONT = pygame.font.SysFont('Arial', 24)

# 色定義（RGB）
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CHAIR_COLOR = (255, 0, 0)              # 椅子の通常色（未使用）
DISABLED_CHAIR_COLOR = (200, 200, 200) # 使用済み椅子の色（灰色）
BORDER_COLOR = (0, 0, 0)               # 枠線の色（黒）
BORDER_WIDTH = 3                       # 枠線の太さ

# テキストを指定座標に描画する汎用関数
def draw_text(screen, text, font, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# 椅子ボタン群（1〜12）を円形に描画する
def draw_chair_buttons(screen, available_chairs, center_x, center_y, radius):
    chair_size = 45  # 各椅子のサイズ（正方形）
    for i in range(12):
        angle = math.radians(i * 30)  # 30度ずつ配置（360 / 12）
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        rect_x = x - chair_size // 2
        rect_y = y - chair_size // 2

        # 椅子の描画（使用可能かどうかで色分け）
        if i + 1 in available_chairs:
            pygame.draw.rect(screen, WHITE, (rect_x, rect_y, chair_size, chair_size))
        else:
            pygame.draw.rect(screen, DISABLED_CHAIR_COLOR, (rect_x, rect_y, chair_size, chair_size))

        # 椅子の周囲に黒い枠線を描画
        pygame.draw.rect(screen, BORDER_COLOR, 
                         (rect_x - BORDER_WIDTH, rect_y - BORDER_WIDTH, 
                          chair_size + 2 * BORDER_WIDTH, chair_size + 2 * BORDER_WIDTH), 
                         BORDER_WIDTH)

        # 椅子の中央に椅子番号を表示（1〜12）
        chair_text = FONT.render(str(i + 1), True, BLACK)
        text_rect = chair_text.get_rect(center=(x, y))
        screen.blit(chair_text, text_rect)

# ゲーム中のメッセージ（主に守り手に椅子選択を促す）を下部に表示する
def prompt_defender_choice(screen, message, font):
    draw_text(screen, message, font, BLACK, 20, 500)
