# game_state.py
# 最終チェック済み ✅
# ゲームの状態（プレイヤー、ターン、椅子の状態）を管理するモジュール。

from player import Player

class GameState:
    def __init__(self):
        # プレイヤーの初期化（0番と1番の2人のプレイヤー）
        self.players = [Player(0), Player(1)]
        self.current_player_index = 0  # 現在のプレイヤーインデックス（0: 攻撃側, 1: 防御側）
        self.available_chairs = list(range(1, 13))  # 使用可能な椅子（1〜12番）
        self.defender_choice = None  # 防御側が選んだ椅子
        self.awaiting_defender = True  # 防御側の椅子選択を待機中かどうか
        self.effect_active = False  # 電撃エフェクトがアクティブかどうか
        self.effect_start_time = None  # 電撃エフェクト開始時刻
        self.shocked = False  # プレイヤーが感電したかどうか

    def switch_turn(self):
        """
        ターンを切り替えるメソッド。
        現在のプレイヤーインデックスを切り替え、次のターンの準備を整える。
        """
        self.current_player_index = 1 - self.current_player_index  # 現在のプレイヤーインデックスを交代
        self.defender_choice = None  # 防御側の椅子選択をリセット
        self.awaiting_defender = True  # 防御側の選択を待機状態に戻す

    def current_player(self):
        """
        現在のプレイヤーを返すメソッド。
        攻撃側または防御側のプレイヤーオブジェクトを返す。
        """
        return self.players[self.current_player_index]

    def opponent_player(self):
        """
        対戦相手（現在のプレイヤーの反対側）のプレイヤーを返すメソッド。
        """
        return self.players[1 - self.current_player_index]
