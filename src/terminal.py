import curses
from time import sleep
from random import randint, choice
import string

# Configuration des couleurs et des caractères
def init_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Texte principal
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Texte secondaire (queue)

def get_random_char():
    """Retourne un caractère aléatoire (lettres, chiffres, symboles)."""
    return choice(string.ascii_letters + string.digits + "!@#$%^&*()_+~<>?")

def random_length(max_length):
    return randint(1, max_length)

def main(stdscr):
    curses.curs_set(0)  # Cacher le curseur
    init_colors()

    # Obtenir les dimensions du terminal
    max_y, max_x = stdscr.getmaxyx()

    # Initialisation des colonnes
    columns = [{'y': randint(-20, 0)*1.0, 'speed': randint(100, 3000)/1000, 'tail_length':random_length(7)} for _ in range(max_x)]
    stdscr.clear()

    while True:
        stdscr.clear()
        for x in range(max_x):
            col = columns[x]
            col['y'] += col['speed']
            
            if col['y'] > max_y:  # Réinitialiser la colonne si elle dépasse l'écran
                col['y'] = randint(-20, 0) * 1.0
                col['speed'] = randint(100, 3000)/1000
                col['tail_length'] = random_length(7)

            # Dessiner la "queue" avec une gradation
            for i in range(col['tail_length']):
                char_y = int(col['y'] - i)
                if 0 <= char_y < max_y and 0 <= x < max_x:  # Vérification stricte des limites
                    char = get_random_char()
                    try:
                        color = 1 if i == 0 else 2
                        stdscr.addch(char_y, x, char, curses.color_pair(color))
                    except curses.error:
                        # Ignorer les erreurs si un caractère est invalide ou si la position est incorrecte
                        pass

        stdscr.refresh()  # Actualiser l'écran
        sleep(0.05)  # Réguler la vitesse globale de l'animation