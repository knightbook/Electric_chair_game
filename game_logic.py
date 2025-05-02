from electric_shock import handle_electric_shock
from scoring import update_score

def play_turn(attacker, defender, player_scores, player_electric_shocks, available_chairs, turn_scores, chair_choice, electric_chair):
    # 電流処理
    game_active = handle_electric_shock(attacker, chair_choice, electric_chair, player_electric_shocks)
    
    # 電流を受けた場合、椅子は場に残る
    if not game_active:
        print(f"💀 プレイヤー{attacker + 1}は電流を3回受けたため敗退しました！")
        turn_scores[attacker].append(0)
        # 電流が流れた椅子は除外しない
        return False, player_scores, player_electric_shocks

    # 電流が流れている椅子を選んだ場合、得点しない
    if chair_choice == electric_chair:
        print(f"守り側の椅子{chair_choice}に電流が流れているため、得点にはなりません。")
        return True, player_scores, player_electric_shocks

    # 得点処理（electric_chairを引き渡す）
    update_score(attacker, chair_choice, player_scores, turn_scores, electric_chair)
    print(f"✅ 椅子 {chair_choice} に座り、{chair_choice} 点獲得！現在の得点: {player_scores[attacker]} 点")

    # 得点された椅子のみを除外
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
