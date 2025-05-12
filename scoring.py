# scoring.py
def update_score(player, chair_choice, electric_chair):
    score = chair_choice  # 椅子番号がそのまま得点
    player.score += score
    player.turn_scores.append(score)
