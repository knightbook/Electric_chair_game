# electric_shock.py
def handle_electric_shock(attacker, chair_choice, electric_chair, player_electric_shocks):
    if chair_choice == electric_chair:
        player_electric_shocks[attacker] += 1
        if player_electric_shocks[attacker] >= 3:
            return False  # Player is out
    return True
