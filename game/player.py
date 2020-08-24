import pygame

from core.logger import logger
from game.constants import MAX_COUNT_CARD_IN_ARM


class Player(object):
    def __init__(self, name):
        self.__hand = pygame.sprite.Group()
        self._active_card = None
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def active_card(self):
        return self._active_card

    @active_card.setter
    def active_card(self, card):
        self._active_card = card

    @active_card.deleter
    def active_card(self):
        self._active_card = None

    @property
    def hand(self):
        return self.__hand

    def add_cart(self, card):
        if self.len_hand >= MAX_COUNT_CARD_IN_ARM:
            logger.warning('Max count card in arm!')
            return
        self.__hand.add(card)

    def remove_card(self, card):
        return self.__hand.remove(card)

    @property
    def len_hand(self):
        return len(self.hand)
