# player.py

class Player:
    def __init__(self, player_id):
        self.id = player_id
        self.score = 0
        self.electric_shocks = 0
        self.turn_scores = []

    def add_score(self, points):
        self.score += points
        self.turn_scores.append(points)

    def receive_shock(self):
        self.electric_shocks += 1
