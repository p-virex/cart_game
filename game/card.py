import os
from pprint import pprint

import pygame

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
        self.image = self.load_image((100, 150))  # 100 x 150 scale 5
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

    def load_image(self, size):
        path = os.path.normpath(os.path.join(os.getcwd(), 'res/carts/{}.png'.format(self.name)))
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size)

    def set_position(self, pos):
        self.rect.x, self.rect.y = pos

    def change_scale(self, h, w, len_arm):
        current_h, current_w = self.image.get_size()
        if current_h == h and current_w == w:
            return
        self.image = self.load_image((h, w))
        # w_shift = 595 if w > 150 else 645
        # self.set_position((105 * len_arm + 5, w_shift))

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return self.name
