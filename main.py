import pygame
import math
from game_logic import play_turn, check_game_over
from chair_buttons import draw_chair_buttons
from text_drawer import draw_text
from prompt_defender import prompt_defender_choice

pygame.init()

# 定数の設定
FONT = pygame.font.SysFont('Arial', 24)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CENTER_X, CENTER_Y = 400, 300
RADIUS = 150

# 状態変数の初期化
current_player = 0  # 0: プレイヤー1, 1: プレイヤー2
available_chairs = list(range(1, 13))  # 椅子1〜12が使用可能
player_scores = [0, 0]  # プレイヤーの得点
player_electric_shocks = [0, 0]  # プレイヤーの電流回数
turn_scores = [[], []]  # 各プレイヤーのターンごとの得点
defender_choice = None  # 守り側が選んだ椅子

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Electric Chair Game")

def game_loop():
    global current_player, player_scores, player_electric_shocks, available_chairs, turn_scores, defender_choice

    running = True
    clock = pygame.time.Clock()
    awaiting_defender = True  # 初めは守り側の選択を待つ

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
                            if awaiting_defender:
                                # 守り側の処理（椅子に電流を流す）
                                defender_choice = chair_num
                                awaiting_defender = False  # 後攻の選択が完了したら攻め側にターンを切り替え
                                print(f"守り側 プレイヤー{1 - current_player + 1} が椅子{chair_num} に電気を流しました（非公開）")
                            else:
                                # 攻め側の選択と得点処理
                                print(f"攻め側 プレイヤー{current_player + 1} が椅子{chair_num} を選びました")
                                game_active, player_scores, player_electric_shocks = play_turn(
                                    current_player, 1 - current_player,
                                    player_scores, player_electric_shocks,
                                    available_chairs, turn_scores,
                                    chair_num, defender_choice
                                )

                                if not game_active:
                                    running = False  # ゲームが終了したらループを抜ける
                                    break

                                # ゲーム終了条件を確認
                                if check_game_over(player_scores, player_electric_shocks):
                                    running = False  # ゲームが終了した場合はループを抜ける
                                    break

                                # ターンが終わった後の状態更新
                                current_player = 1 - current_player  # プレイヤーのターンを切り替え
                                defender_choice = None  # 次のターンに備えて守り側の椅子選択をリセット
                                awaiting_defender = True  # 次のターンで守り側の選択を待つ

        # 画面描画
        draw_chair_buttons(screen, available_chairs, CENTER_X, CENTER_Y, RADIUS)
        draw_text(screen, f"ターン: {len(turn_scores[0]) + len(turn_scores[1]) + 1}", FONT, BLACK, 20, 20)
        draw_text(screen, f"プレイヤー1: {player_scores[0]}点 | プレイヤー2: {player_scores[1]}点", FONT, BLACK, 20, 60)

        # 守り側か攻め側かのメッセージを描画
        prompt_text = "守り側の椅子を選択してください" if awaiting_defender else "攻め側の椅子を選択してください"
        prompt_defender_choice(screen, prompt_text, FONT)

        pygame.display.update()  # 画面の更新
        clock.tick(30)  # FPSを30に設定

    pygame.quit()  # ゲーム終了時にpygameを終了

if __name__ == "__main__":
    game_loop()  # ゲームループの開始
