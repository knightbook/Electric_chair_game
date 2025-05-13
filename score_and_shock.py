# score_and_shock.py
def handle_shock_and_score(player, chair_choice, electric_chair):
    score = chair_choice  # 椅子番号がそのまま得点
    player.score += score
    player.turn_scores.append(score)

    if chair_choice == electric_chair:
        player.electric_shocks += 1
        if player.electric_shocks >= 3:
            return False  # 3回感電で敗北
    return True  # 感電しなかった or まだ敗北条件に達していない
