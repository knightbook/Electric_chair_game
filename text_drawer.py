#text_drawer.py
import pygame

# 画面にテキストを描画するための関数
def draw_text(screen, text, font, color, x, y):
    # 引数で渡されたテキストを指定のフォントと色で描画可能なオブジェクトに変換
    label = font.render(text, True, color)
    
    # 画面（screen）にそのテキストを指定した座標 (x, y) に描画
    screen.blit(label, (x, y))
