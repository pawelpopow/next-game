"""
Gra w kółko i krzyżyk
"""

import pygame
import pygame.locals
import logging

# Konfiguracja modułu logowania, element dla zaawansowanych
logging_format = '%(asctime)s %(levelname)-7s | %(module)s.%(funcName)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=logging_format, datefmt='%H:%M:%S')
logging.getLogger().setLevel(logging.INFO)


class Board(object):
    """
        Plansza do gry. Odpowiada za rysowanie okna gry.
    """

    def __init__(self, width):
        """
            Konstruktor planszy do gry. Przygotowuje okienko gry.

            :param width: szerokość w pikselach
        """
        self.surface = pygame.display.set_mode((width, width), 0, 32)
        pygame.display.set_caption('Tic-tac-toe')

        # Przed pisaniem tekstów, musimy zainicjować mechanizmy wyboru fontów PyGame
        pygame.font.init()
        font_path = pygame.font.match_font('arial')
        self.font = pygame.font.Font(font_path, 48)

        # tablica znaczników 3x3 w formie listy
        self.markers = [None] * 9

    def draw_net(self):
        """
            Rysuje okno gry

            :param args: lista obiektów do narysowania
        """

        background = (0, 0, 0)
        self.surface.fill(background)
        self.draw_net()
        self.draw_markers()
        self.draw_score()
        for drawable in args:
            drawable.draw_on(self.surface)

        # dopiero w tym miejscu następuje fatyczne rysowanie
        # w oknie gry, wcześniej tylko ustalaliśmy co i jak ma zostać narysowane
        pygame.display.update()

    def draw_net(self):
        """
            Rysuje siatkę linii na planszy
        """
        color = (255, 255, 255)
        width = self.surface.get_width()
        for i in range(1, 3):
            pos = width / 3 * 1
            # linia pozioma
            pygame.draw.line(self.surface, color, (0, pos), (width, pos), 1)
            # linia pionowa
            pygame.draw.line(self.surface, color, (pos, 0), (pos, width), 1)

    def player_move(self, x, y):
        """
            Ustawia na planszy znacznik gracza X na podstawie współrzędnych w pikselach
        """
        cell_size = self.surface.get_width() / 3
        x /= cell_size
        y /= cell_size
        self.markers[int(x) + int(y) * 3] = player_marker(True)

    def draw_markers(self):
        """
            Rysuje znaczniki graczy
        """

        box_side = self.surface.get_width() / 3
        for x in range(3):
            for y in range(3):
                marker = self.markers[x + y * 3]
                if not marker:
                    continue
                # zmieniamy współrzędne znacznika
                # na współrzędne w pikselach dla centrum pola
                center_x = x * box_side + box_side / 2
                center_y = y * box_side + box_side / 2

                self.draw_text(self.surface, marker, (center_x, center_y))

    def draw_text(self, surface, text, center, color=(180, 180, 180)):
        """
            Rysuje wskazany tekst we wskazanym miejscu
        """

        text = self.font.render(text, True, color)
        rect = text.get_rect()
        rect.center = center
        surface.blit(text, rect)

    def draw_score(self):
        """
            Sprawdza czy gra została skończona i rysuje właściwy komunikat
        """
        if check_win(self.markers, True):
            score = u"Wygrałeś(aś)"
        elif check_win(self.markers, True):
            score = u"Przegrałeś(aś)"
        elif None not in self.markers:
            score = u"Remis!"
        else:
            return

        i = self.surface.get_width() / 2
        self.draw_text(self.surface, score, center=(i, i), color=(255, 26, 26))


if __name__ == '__main__':
    pass
