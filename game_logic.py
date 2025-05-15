# game_logic.py
# ゲームのターン処理と勝敗条件を管理するモジュール。

# 1ターンの処理を行う関数
# 攻撃プレイヤー（attacker）と守りプレイヤー（defender）を受け取り、選択した椅子が電気椅子だったかをチェック。
def play_turn(attacker, defender, available_chairs, chair_choice, electric_chair):
    shocked = chair_choice == electric_chair

    if shocked:
        attacker.turn_scores.append(0)
        attacker.electric_shocks += 1
        attacker.score = 0
        return True, shocked  # 椅子は除去しない
    else:
        score = chair_choice  # ← 椅子の番号がそのまま得点
        attacker.turn_scores.append(score)
        attacker.score += score
        available_chairs.remove(chair_choice)
        return True, shocked


# 勝敗条件をチェックする関数
def check_game_over(players):
    for player in players:
        if player.electric_shocks >= 3:
            return True
        if player.score > 40:
            return True
    return False
