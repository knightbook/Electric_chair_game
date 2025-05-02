from prettytable import PrettyTable

def display_scoreboard(turn_scores, player_scores, player_electric_shocks):
    table = PrettyTable()
    max_turns = 8

    # 見出しの作成
    field_names = ["プレイヤー"] + [f"ターン{i+1}" for i in range(max_turns)] + ["合計得点", "電流回数"]
    table.field_names = field_names

    for i in range(2):
        padded_scores = turn_scores[i] + [""] * (max_turns - len(turn_scores[i]))
        table.add_row([i + 1] + padded_scores + [player_scores[i], player_electric_shocks[i]])

    print("\n最終スコアボード:")
    print(table)
