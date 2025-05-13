#main.py
import pygame
import math
import random
import os

from game_logic import play_turn, check_game_over
from chair_buttons import draw_chair_buttons
from ui_elements import draw_title, draw_rules_plate, draw_prompt

from scoreboard import display_scoreboard

from game_state import GameState  # Playerはgame_state内で扱う

pygame.init()

# --- 定数定義 ---
font_path = os.path.join('font', 'DotGothic16-Regular.ttf')  # 'font' フォルダ内のフォント
TITLE_FONT = pygame.font.Font(font_path, 40)
FONT = pygame.font.Font(font_path, 24)

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
CENTER_X, CENTER_Y = 300, 300
RADIUS = 150

# --- ウィンドウ初期化 ---
screen = pygame.display.set_mode((950, 650))
pygame.display.set_caption("Electric Chair Game")



# --- 電撃エフェクト描画 ---
def draw_electric_shock_effect(screen, elapsed_time):
    if elapsed_time < 1500:
        for _ in range(10):
            start_x = CENTER_X + random.randint(-150, 150)
            start_y = CENTER_Y + random.randint(-150, 150)
            end_x = CENTER_X + random.randint(-150, 150)
            end_y = CENTER_Y + random.randint(-150, 150)
            pygame.draw.line(screen, (255, 255, 0), (start_x, start_y), (end_x, end_y), 5)
        return True
    return False


# --- メインゲームループ ---
def game_loop():
    game_state = GameState()  # 状態を初期化
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(GRAY)
        draw_title(screen, TITLE_FONT)

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
        draw_prompt(screen, prompt_text, FONT)  # draw_promptを使って表示
        draw_rules_plate(screen, FONT)
        pygame.display.update()
        clock.tick(30)

    pygame.quit()


# --- 実行 ---
if __name__ == "__main__":
    game_loop()
