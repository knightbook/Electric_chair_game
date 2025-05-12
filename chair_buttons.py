#chair_buttons.py
import pygame
import math

# pygameの初期化（必要な内部処理をスタート）
pygame.init()

# フォントの定義（pygame.init()の後でないとエラーになる）
FONT = pygame.font.SysFont('Arial', 24)

# テキストを画面に描画する関数
def draw_text(screen, text, font, color, x, y):
    # 指定されたフォントと色でテキストをレンダリング
    label = font.render(text, True, color)
    # 指定座標(x, y)にテキストを描画
    screen.blit(label, (x, y))

# 色の定義を追加
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CHAIR_COLOR = (255, 0, 0)  # 椅子の色（赤色）
DISABLED_CHAIR_COLOR = (200, 200, 200)  # 使用不可椅子の色（灰色）
BORDER_COLOR = (0, 0, 0)  # 枠線の色（黒色）
BORDER_WIDTH = 3  # 枠線の太さ

# 椅子ボタン（円周に配置されたボタン）を描画する関数
def draw_chair_buttons(screen, available_chairs, center_x, center_y, radius):
    chair_size = 45  # 椅子のサイズ（四角形）
    for i in range(12):
        # 角度に基づいて椅子の位置を計算
        angle = math.radians(i * 30)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        # 四角形の中心座標を調整
        rect_x = x - chair_size // 2
        rect_y = y - chair_size // 2

        # 四角形の椅子を描画
        if i + 1 in available_chairs:
            pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, chair_size, chair_size))
        else:
            pygame.draw.rect(screen, (200, 200, 200), (rect_x, rect_y, chair_size, chair_size))  # 使用不可椅子

        # 椅子の枠線を描画（椅子のサイズより少し大きい枠線）
        pygame.draw.rect(screen, BORDER_COLOR, (rect_x - BORDER_WIDTH, rect_y - BORDER_WIDTH, chair_size + 2 * BORDER_WIDTH, chair_size + 2 * BORDER_WIDTH), BORDER_WIDTH)

        # 椅子番号を表示（中央に）
        chair_text = FONT.render(str(i + 1), True, BLACK)
        text_rect = chair_text.get_rect(center=(x, y))
        screen.blit(chair_text, text_rect)

# 守り手の選択肢を促すメッセージを画面に表示する関数
def prompt_defender_choice(screen, message, font):
    # 画面下部（y=500）にメッセージを描画
    draw_text(screen, message, font, (0, 0, 0), 20, 500)
