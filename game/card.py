import os

import pygame

from game.constants import RANK_INDEX_NAME, COLOUR_INDEX_NAME


class Card:
    def __init__(self, colour, rank):
        """
        :param colour:  масть карты от 0 до 3
        :param rank:  ранг карты от 1 до 13
        """
        self.__colour = colour
        self.__rank = rank
        self.__name_card = '{}_of_{}'.format(RANK_INDEX_NAME[rank], COLOUR_INDEX_NAME[colour])
        self.__image = self.load_image()  # 100 x 145 scale 5

    @property
    def rank(self):
        return self.__rank

    @property
    def colour(self):
        return self.__colour

    @property
    def name(self):
        return self.__name_card

    @property
    def image(self):
        return self.__image

    def load_image(self):
        path = os.path.normpath(os.path.join(os.getcwd(), 'res/carts/{}.png'.format(self.name)))
        return pygame.image.load(path)
