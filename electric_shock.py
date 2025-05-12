# electric_shock.py

# 攻撃プレイヤーが選んだ椅子に電気が流れていた場合の処理を行う関数
def handle_electric_shock(player, chair_choice, electric_chair):
    if chair_choice == electric_chair:
        player.electric_shocks += 1
        if player.electric_shocks >= 3:
            return False  # プレイヤー敗退
    return True
