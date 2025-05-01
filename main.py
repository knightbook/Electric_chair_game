import pygame
import math
from game_logic import play_turn, check_game_over
from scoreboard import display_scoreboard  # 必要に応じて使用
from ui import draw_text, draw_chair_buttons

# 初期化
pygame.init()

# 定数
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont('Arial', 24)
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
RADIUS = 150

# ゲーム設定
current_player = 0
available_chairs = list(range(1, 13))
player_scores = [0, 0]
player_electric_shocks = [0, 0]
turn_scores = [[], []]

# 画面作成
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Electric Chair Game")

def game_loop():
    global current_player, player_scores, player_electric_shocks, available_chairs, turn_scores

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for i in range(12):
                    angle = math.radians(i * 30)
                    x = CENTER_X + RADIUS * math.cos(angle)
                    y = CENTER_Y + RADIUS * math.sin(angle)
                    if (mouse_x - x) ** 2 + (mouse_y - y) ** 2 <= 25 ** 2:
                        chair_num = i + 1
                        if chair_num in available_chairs:
                            print(f"プレイヤー{current_player + 1}が椅子{chair_num}を選びました！")
                            game_active, player_scores, player_electric_shocks = play_turn(
                                current_player, 1 - current_player, player_scores, player_electric_shocks, available_chairs, turn_scores, chair_num
                            )
                            if not game_active or check_game_over(player_scores, player_electric_shocks):
                                running = False
                                break
                            current_player = 1 - current_player

        draw_chair_buttons(screen, CENTER_X, CENTER_Y, RADIUS, FONT, available_chairs)
        draw_text(screen, f"ターン: {len(turn_scores[0]) + len(turn_scores[1]) + 1}", FONT, BLACK, 20, 20)
        draw_text(screen, f"プレイヤー1: {player_scores[0]}点 | プレイヤー2: {player_scores[1]}点", FONT, BLACK, 20, 60)

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
