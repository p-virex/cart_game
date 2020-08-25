import pygame

from core.logger import logger
from game.constants import MAX_COUNT_CARD_IN_ARM


class Player(object):
    def __init__(self, name):
        self.__hand = pygame.sprite.Group()
        self._active_card = None
        self.__name = name

    def bot_first_turn(self, trump_card):
        """
        Первая карта для хода бота, выбирается самая маленькая не козырная
        """
        min_card = None
        for card in self.hand:
            if card.colour == trump_card.colour:
                continue
            if not min_card:
                min_card = card
            if card.rank < min_card.rank:
                min_card = card
        logger.info(f'Bot turn card: {min_card.name}')
        return min_card

    def player_turn(self, game):
        print(game.attack, game.defend)
        if game.attack:
            game.add_card_in_game_deck(self.active_card)
            self.remove_card(self.active_card)
            del self.active_card
            game.defend, game.attack = True, False

    def player_defend_event(self, game):
        last_card = game.last_card_in_game_deck
        if self.check_rank(last_card) and self.check_colour(last_card) or self.check_trump(game) and not game.defend:
            game.add_card_in_game_deck(self.active_card)
            self.remove_card(self.active_card)
            del self.active_card
            game.defend, game.attack = True, False
        logger.info(f'Active card: {game.last_card_in_game_deck.name}')

    def check_rank(self, card):
        if card.rank < self.active_card.rank:
            return True
        return

    def check_trump(self, game):
        if self.active_card.colour == game.trump_card.colour:
            return True
        return

    def check_colour(self, card):
        if card.colour == self.active_card.colour:
            return True
        return

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
        logger.info(f'{self.name}, add card: {card.name}')
        self.__hand.add(card)

    def remove_card(self, card):
        return self.__hand.remove(card)

    @property
    def len_hand(self):
        return len(self.hand)
