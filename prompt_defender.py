# prompt_defender.py
from text_drawer import draw_text

def prompt_defender_choice(screen, message, font):
    draw_text(screen, message, font, (0, 0, 0), 20, 500)
