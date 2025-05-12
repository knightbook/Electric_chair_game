#scoreboard.py
import pygame

def display_scoreboard(screen, turn_scores, player_scores, player_electric_shocks, font, screen_width):
    max_turns = 8
    board_height = 120
    board_top = screen.get_height() - board_height
    cell_height = 40
    line_color = (255, 255, 255)
    board_color = (50, 50, 50)
    static_text_color = (255, 0, 0)      # 赤（固定文字）
    dynamic_text_color = (255, 255, 255) # 白（スコアなど動的な数値）

    # 列幅リスト（P:40, T1〜T8:60ずつ, 合計点:80, 電流回数:80）
    cell_widths = [40] + [60] * max_turns + [80, 80]
    total_column_width = sum(cell_widths)  # 列幅の合計

    # 画面幅に合わせて最後の列の幅を調整
    total_width = screen_width
    if total_column_width < total_width:
        diff = total_width - total_column_width
        cell_widths[-1] += diff  # 最後の列（電流回数、合計点）の幅を調整

    # ボード背景
    pygame.draw.rect(screen, board_color, (0, board_top, total_width, board_height))

    # ヘッダー
    headers = ["P"] + [f"T{i+1}" for i in range(max_turns)] + ["合計点", "電流回数"]
    x = 0
    for col, header in enumerate(headers):
        draw_text(screen, header, font, static_text_color, x + 6, board_top + 4)
        pygame.draw.rect(screen, line_color, (x, board_top, cell_widths[col], cell_height), 1)
        x += cell_widths[col]

    # 各プレイヤーのスコア
    for row in range(2):
        padded_scores = turn_scores[row] + [""] * (max_turns - len(turn_scores[row]))
        data = [str(row + 1)] + [str(s) for s in padded_scores] + [str(player_scores[row]), str(player_electric_shocks[row])]
        x = 0
        y = board_top + cell_height * (row + 1) + 5
        for col, text in enumerate(data):
            color = dynamic_text_color if 1 <= col <= max_turns else static_text_color
            draw_text(screen, text, font, color, x + 5, y)
            pygame.draw.rect(screen, line_color, (x, y - 5, cell_widths[col], cell_height), 1)
            x += cell_widths[col]

def draw_text(screen, text, font, color, x, y):
    label = font.render(str(text), True, color)
    screen.blit(label, (x, y))
