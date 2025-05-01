from prettytable import PrettyTable

def display_scoreboard(turn_scores, player_scores, player_electric_shocks):
    table = PrettyTable()

    # スコアボードの設定（プレイヤーごとのターン得点、合計点、電流回数）
    table.field_names = ["プレイヤー", "ターン1", "ターン2", "ターン3", "ターン4", "ターン5", "ターン6", "ターン7", "ターン8", "合計得点", "電流回数"]

    # プレイヤー1のターン得点と合計を追加
    table.add_row([1] + turn_scores[0] + [player_scores[0], player_electric_shocks[0]])

    # プレイヤー2のターン得点と合計を追加
    table.add_row([2] + turn_scores[1] + [player_scores[1], player_electric_shocks[1]])

    print("\n最終スコアボード:")
    print(table)
