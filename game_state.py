#gema_state.py
from player import Player
class GameState:
    def __init__(self):
        self.players = [Player(0), Player(1)]
        self.current_player_index = 0  # 現在のプレイヤーインデックスを保持
        self.available_chairs = list(range(1, 13))
        self.defender_choice = None
        self.awaiting_defender = True
        self.effect_active = False
        self.effect_start_time = None
        self.shocked = False

    def switch_turn(self):
        self.current_player_index = 1 - self.current_player_index
        self.defender_choice = None
        self.awaiting_defender = True

    # current_playerは属性として扱う
    def current_player(self):
        return self.players[self.current_player_index]

    # opponent_playerもインデックスでアクセス
    def opponent_player(self):
        return self.players[1 - self.current_player_index]
