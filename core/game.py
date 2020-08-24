from random import random

import pygame

from core.logger import logger
from game.constants import POS_TRAMP_CARD, RANK_INDEX_NAME, COUNT_START_CARD, POS_GAME_DECK


class GameController:
    def __init__(self, render, deck):
        self.__players = list()
        self.__client_player = None
        self.render = render
        self.deck = deck
        self.__trump_card = None
        self.__last_card = None
        self.__game_deck = pygame.sprite.Group()

    def game(self):
        pass

    def check_first_attacker(self):
        player_attack = None
        min_trump_card = None
        for player in self.__players:
            for card in player.hand:
                if card.colour == self.__trump_card.colour:
                    if not min_trump_card:
                        min_trump_card = card
                        player_attack = player
                    else:
                        if min_trump_card.rank < card.rank:
                            min_trump_card = card
                            player_attack = player

        if player_attack and min_trump_card:
            logger.info(f'Attack player: {player_attack.name}, min trump card: {min_trump_card.name}')
        else:
            logger.warning('Players don\'t have trump card!')
            player_attack = self.__players[0]
            logger.info(f'Random choice attack player: {player_attack.name}')
        return player_attack

    def set_trump_card(self):
        self.__trump_card = self.deck.get_card
        if RANK_INDEX_NAME[self.__trump_card.rank] == 'ace':
            logger.warning(f'Ace for trump card: {self.__trump_card.name}')
            self.deck.return_card_in_deck(self.__trump_card)
            # todo: fix me
            self.__trump_card = self.deck.get_card
            logger.warning(f'New trump card: {self.__trump_card.name}')
        logger.info(f'Set trump card: {self.__trump_card.name}')

    def render_trump_card(self):
        self.render.render_image(self.__trump_card.image, POS_TRAMP_CARD)

    def set_client_player(self, player):
        self.__client_player = player

    def add_start_card(self, player):
        for i in range(COUNT_START_CARD):
            card = self.deck.get_card
            player.add_cart(card)
        if player == self.__client_player:
            self.render.draw_pl_cards()
        self.__players.append(player)

    def add_card_in_game_deck(self, card):
        self.__game_deck.add(card)
        card.set_position(POS_GAME_DECK)
        logger.debug(f'Name: {card.name}, pos: {card.rect}')

    @property
    def game_deck(self):
        return self.__game_deck

    @property
    def len_game_deck(self):
        return len(self.__game_deck)

