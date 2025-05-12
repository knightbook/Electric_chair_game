# prompt_defender.py
# 守り側プレイヤーに対して椅子選択のメッセージを画面に描画する関数

from text_drawer import draw_text  # テキスト描画用の関数をインポート

def prompt_defender_choice(screen, message, font):
    # 指定したメッセージを画面下部（y=500）に黒色で表示する
    draw_text(screen, message, font, (0, 0, 0), 20, 500)
