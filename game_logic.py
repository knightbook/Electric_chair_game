# game_logic.py
# 最終チェック済み ✅
# ゲームのターン処理と勝敗条件を管理するモジュール。

from score_and_shock import handle_shock_and_score


# 1ターンの処理を行う関数
# 攻撃プレイヤー（attacker）と守りプレイヤー（defender）を受け取り、選択した椅子が電気椅子だったかをチェック。
def play_turn(attacker, defender, available_chairs, chair_choice, electric_chair):
    shocked = chair_choice == electric_chair
    game_active = handle_shock_and_score(attacker, chair_choice, electric_chair)

    if shocked:
        attacker.score = 0
        attacker.turn_scores[-1] = 0  # スコア履歴の修正

    if not game_active:
        return False, shocked

    available_chairs.remove(chair_choice)

    return True, shocked


# 勝敗条件をチェックする関数
# プレイヤーが感電回数3回以上またはスコア40以上でゲームオーバー
def check_game_over(players):
    for player in players:
        if player.electric_shocks >= 3:
            return True  # 3回感電したプレイヤーがいる場合、ゲーム終了
        if player.score > 40:
            return True  # スコアが40を超えたプレイヤーがいる場合、ゲーム終了
    return False  # どちらの条件にも該当しない場合、ゲーム続行
