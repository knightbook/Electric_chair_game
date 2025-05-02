def update_score(attacker, chair_choice, player_scores, turn_scores, electric_chair):
    if chair_choice != electric_chair:
        player_scores[attacker] += chair_choice
        turn_scores[attacker].append(chair_choice)
        print(f"プレイヤー{attacker + 1}が椅子{chair_choice}に座り、得点が追加されました！")
    else:
        print(f"守り側の椅子{electric_chair}に電流が流れているため、得点にはなりません。")
