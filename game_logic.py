#game_logic.py
from electric_shock import handle_electric_shock
from scoring import update_score

# 1ターンの処理を行う関数（Playerインスタンスを直接受け取る）
def play_turn(attacker, defender, available_chairs, chair_choice, electric_chair):
    shocked = False

    # 電撃処理（生存したかどうか）
    game_active = handle_electric_shock(attacker, chair_choice, electric_chair)

    if not game_active:
        shocked = True
        attacker.turn_scores.append(0)
        return False, shocked

    if chair_choice == electric_chair:
        shocked = True
        attacker.score = 0  # 電流が流れた場合、スコアをリセット
        attacker.turn_scores.append(0)
        return True, shocked

    # 電流が流れなかった場合、座った椅子のポイントを加算
    update_score(attacker, chair_choice, electric_chair)
    available_chairs.remove(chair_choice)

    return True, shocked

# 勝敗条件チェック（Playerインスタンスのリストを受け取る）
def check_game_over(players):
    for player in players:
        if player.electric_shocks >= 3:
            return True
        if player.score > 40:
            return True
    return False

