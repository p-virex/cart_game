import pygame

from core.logger import logger
from core.service import load_image_card
from game.constants import RANK_INDEX_NAME, COLOUR_INDEX_NAME


class Card(pygame.sprite.Sprite):
    def __init__(self, colour, rank):
        pygame.sprite.Sprite.__init__(self)
        """
        :param colour:  масть карты от 0 до 3
        :param rank:  ранг карты от 1 до 13
        """
        self.__colour = colour
        self.__rank = rank
        self.__name_card = '{}_of_{}'.format(RANK_INDEX_NAME[rank], COLOUR_INDEX_NAME[colour])
        self.image = load_image_card((100, 150), self.name)  # 100 x 150 scale 5
        self.rect = self.image.get_rect()

    @property
    def rank(self):
        return self.__rank

    @property
    def colour(self):
        return self.__colour

    @property
    def name(self):
        return self.__name_card

    def set_position(self, pos):
        self.rect.x, self.rect.y = pos

    def change_scale(self, h, w, skip_check=False):
        current_h, current_w = self.image.get_size()
        if current_h == h and current_w == w and not skip_check:
            return
        self.image = load_image_card((h, w), self.name)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return self.name


class DeckBackOfCard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image_card((150, 200), 'back_of_a_card')  # 100 x 150 scale 5
        self.rect = self.image.get_rect()
        self.rect.x = 1025
        self.rect.y = 270

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
