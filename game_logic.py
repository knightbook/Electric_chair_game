def play_turn(attacker, defender, player_scores, player_electric_shocks, available_chairs, turn_scores, chair_choice, electric_chair):
    if chair_choice == electric_chair:
        player_electric_shocks[attacker] += 1
        print(f"⚡ 電流をくらいました！プレイヤー{attacker + 1} はこれで {player_electric_shocks[attacker]} 回目です。")
        if player_electric_shocks[attacker] >= 3:
            print(f"💀 プレイヤー{attacker + 1} は電流を3回受けたため敗退しました！")
            turn_scores[attacker].append(0)
            available_chairs.remove(chair_choice)
            return False, player_scores, player_electric_shocks
        player_scores[attacker] = 0
        turn_scores[attacker].append(0)
    else:
        player_scores[attacker] += chair_choice
        turn_scores[attacker].append(chair_choice)
        print(f"✅ 椅子 {chair_choice} に座り、{chair_choice} 点獲得！現在の得点: {player_scores[attacker]} 点")

    available_chairs.remove(chair_choice)
    return True, player_scores, player_electric_shocks


def check_game_over(player_scores, player_electric_shocks):
    for i in range(2):
        if player_electric_shocks[i] >= 3:
            print(f"💀 プレイヤー{i + 1} は電流を3回受けたため敗北！")
            return True
        if player_scores[i] > 40:
            print(f"🏆 プレイヤー{i + 1} が40点を超えたため勝利！")
            return True
    return False
