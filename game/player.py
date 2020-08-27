import pygame

from core.logger import logger
from game.constants import MAX_COUNT_CARD_IN_ARM, BASE_CARD_WIDTH, BASE_CARD_HEIGHT


class Player(object):
    def __init__(self, name):
        self.__hand = pygame.sprite.Group()
        self._active_card = None
        self.__name = name
        self.__made_turn = None

    def player_turn(self, game):
        if self.active_card.rank in [card.rank for card in game.game_deck]:
            game.add_card_in_game_deck(self.active_card)
            self.remove_card(self.active_card)
            del self.active_card
            self.made_turn = True

    def first_player_turn(self, game):
        game.add_card_in_game_deck(self.active_card)
        self.remove_card(self.active_card)
        del self.active_card
        self.made_turn = True

    def player_defend_event(self, game):
        """
        Событие для защиты от хода бота для игрока.

        Когда игрок защищается, нам надо определить подходит ли выбранная карта для защиты:
            * ранг  должен быть больше чем у той карты что в колоде
            * масть должна совподать
            * или карта должна быть козырем

        :param game: игровой контролер
        """
        if self.made_turn:
            return
        # берем верхнюю карту в игровой колоде
        last_card = game.game_card
        if self.check_rank(last_card) and self.check_colour(last_card) or self.check_trump(game) and game.turn_bot:
            # добовляем в игровую колоду активную карту, удаляем ее из руки игрока и удаляем активную карту
            game.add_card_in_game_deck(self.active_card)
            self.remove_card(self.active_card)
            del self.active_card
            self.made_turn = True
        logger.info(f'Defend card: {game.game_card.name}')

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
    def cards_in_hand(self):
        return ', '.join([card.name for card in self.hand])

    @property
    def name(self):
        return self.__name

    @property
    def made_turn(self):
        return self.__made_turn

    @made_turn.setter
    def made_turn(self, value):
        self.__made_turn = value

    @made_turn.deleter
    def made_turn(self):
        self.__made_turn = None

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
        if card:
            logger.info(f'To hand {self.name}, add card: {card.name}')
            card.change_scale(BASE_CARD_WIDTH, BASE_CARD_HEIGHT)
            self.__hand.add(card)

    def remove_card(self, card):
        return self.__hand.remove(card)

    @property
    def len_hand(self):
        return len(self.hand)
