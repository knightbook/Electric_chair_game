#main.py
import pygame
import math
import random
import time

from game_logic import play_turn, check_game_over
from chair_buttons import draw_chair_buttons
from text_drawer import draw_text
from prompt_defender import prompt_defender_choice
from scoreboard import display_scoreboard

from game_state import GameState  # Playerはgame_state内で扱う

pygame.init()

# --- 定数定義 ---
FONT = pygame.font.Font('C:/Python学習/electric_chair_game/font/DotGothic16-Regular.ttf', 24)
TITLE_FONT = pygame.font.Font('C:/Python学習/electric_chair_game/font/DotGothic16-Regular.ttf', 40)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
CENTER_X, CENTER_Y = 300, 300
RADIUS = 150

# --- ウィンドウ初期化 ---
screen = pygame.display.set_mode((950, 650))
pygame.display.set_caption("Electric Chair Game")

# --- タイトル描画 ---
def draw_title(screen):
    title_text = TITLE_FONT.render("電気椅子ゲーム", True, BLACK)
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 10))

# --- 電撃エフェクト描画 ---
def draw_electric_shock_effect(screen, elapsed_time):
    if elapsed_time < 5000:
        for _ in range(10):
            start_x = CENTER_X + random.randint(-150, 150)
            start_y = CENTER_Y + random.randint(-150, 150)
            end_x = CENTER_X + random.randint(-150, 150)
            end_y = CENTER_Y + random.randint(-150, 150)
            pygame.draw.line(screen, (255, 255, 0), (start_x, start_y), (end_x, end_y), 5)
        return True
    return False
# --- ルールプレートの設置 ---
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

# --- メインゲームループ ---
def game_loop():
    game_state = GameState()  # 状態を初期化
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(GRAY)
        draw_title(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                # 椅子を選択する処理
                for i in range(12):
                    angle = math.radians(i * 30)
                    x = CENTER_X + RADIUS * math.cos(angle)
                    y = CENTER_Y + RADIUS * math.sin(angle)
                    if (mouse_x - x) ** 2 + (mouse_y - y) ** 2 <= 25 ** 2:
                        chair_num = i + 1
                        if chair_num in game_state.available_chairs:
                            if game_state.awaiting_defender:
                                game_state.defender_choice = chair_num
                                game_state.awaiting_defender = False
                            else:
                                # 現在のプレイヤーを取得
                                attacker = game_state.players[game_state.current_player_index]
                                defender = game_state.players[1 - game_state.current_player_index]

                                # ターンの処理（electric_flowは不要）
                                game_active, shocked = play_turn(
                                    attacker, defender,
                                    game_state.available_chairs,
                                    chair_num, game_state.defender_choice
                                )

                                if shocked:
                                    game_state.effect_start_time = pygame.time.get_ticks()
                                    game_state.effect_active = True

                                if not game_active or check_game_over(game_state.players):
                                    running = False
                                    break

                                # ターンの切り替え
                                game_state.switch_turn()
                                game_state.defender_choice = None
                                game_state.awaiting_defender = True

        # エフェクト描画
        if game_state.effect_active:
            elapsed_time = pygame.time.get_ticks() - game_state.effect_start_time
            game_state.effect_active = draw_electric_shock_effect(screen, elapsed_time)

        # 椅子＆スコア描画
        draw_chair_buttons(screen, game_state.available_chairs, CENTER_X, CENTER_Y, RADIUS)
        display_scoreboard(screen, [p.turn_scores for p in game_state.players],
                           [p.score for p in game_state.players],
                           [p.electric_shocks for p in game_state.players],
                           FONT, screen.get_width())

        # プロンプト表示
        prompt_text = "守り側の椅子を選択してください" if game_state.awaiting_defender else "攻め側の椅子を選択してください"
        prompt_defender_choice(screen, prompt_text, FONT)
        draw_rules_plate(screen, FONT)
        pygame.display.update()
        clock.tick(30)

    pygame.quit()


# --- 実行 ---
if __name__ == "__main__":
    game_loop()
