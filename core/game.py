from random import random

import pygame

from core.logger import logger
from game.constants import POS_TRAMP_CARD, RANK_INDEX_NAME, COUNT_START_CARD, POS_GAME_DECK, BIG_CARD_WIDTH, \
    BIG_CARD_HEIGHT, GAME_DECK_WIDTH, GAME_DECK_HEIGHT


class GameController:
    def __init__(self, render, deck):
        self.__players = list()
        self.__client_player = None
        self.render = render
        self.deck = deck
        self.__trump_card = None
        self.__last_card = None
        self.__game_deck = pygame.sprite.Group()
        self.__clear_cards = pygame.sprite.Group()
        self.player_attack = None
        self.player_defend = None
        self.defend = None
        self.attack = None
        self.first_turn = None

    def game(self):
        if not self.first_turn and self.player_attack.name == 'Bot':
            self.first_bot_turn()
            self.first_turn = True
        elif not self.first_turn:
            self.first_player_turn()
            self.first_turn = True

        if self.player_attack.name == 'Bot' and self.defend and not self.attack:
            if not self.next_card_from_bot():
                self.player_defend = self.player_attack
                self.player_attack = self.__client_player
                logger.info(f'Defend: {self.player_defend.name}, attack: {self.player_attack.name}')
                self.clear_game_deck()
                self.check_cards_in_hands()
                self.attack, self.defend = True, False
        if self.player_defend and self.player_defend.name == 'Bot' and self.defend and not self.attack:
            self.defend_bot_card()

    def defend_bot_card(self):
        def_card = None
        for card_in_hand in self.player_defend.hand:
            if card_in_hand.colour == self.last_card_in_game_deck.colour and card_in_hand.rank > self.last_card_in_game_deck.rank:
                def_card = card_in_hand
                self.add_card_in_game_deck(card_in_hand)
                self.player_defend.remove_card(card_in_hand)
                self.attack, self.defend = False, True
                break

    def check_cards_in_hands(self):
        for player in self.__players:
            if player.len_hand < 6:
                logger.info(f'Player: {player.name} have {player.len_hand} in hand')
                for i in range(6 - player.len_hand):
                    player.add_cart(self.deck.get_card)

    def clear_game_deck(self):
        for card in self.game_deck:
            self.__clear_cards.add(card)
        self.__game_deck = pygame.sprite.Group()

    def next_card_from_bot(self):
        for card in self.game_deck:
            for card_in_hand in self.player_attack.hand:
                if card_in_hand.rank == card.rank and card_in_hand.colour != self.trump_card.colour:
                    self.add_card_in_game_deck(card_in_hand)
                    self.player_attack.remove_card(card_in_hand)
                    self.__last_card = card_in_hand
                    self.player_defend = self.__client_player
                    self.attack, self.defend = True, False
                    return True
        return

    def first_player_turn(self):
        self.attack, self.defend = True, False

    def first_bot_turn(self):
        turn_card = self.player_attack.bot_first_turn(self.__trump_card)
        self.add_card_in_game_deck(turn_card)
        self.player_attack.remove_card(turn_card)
        self.__last_card = turn_card
        self.player_defend = self.__client_player
        self.attack, self.defend = True, False

    @property
    def last_card_in_game_deck(self):
        return self.__last_card

    def check_first_attacker(self):
        min_trump_card = None
        for player in self.__players:
            for card in player.hand:
                if card.colour == self.__trump_card.colour:
                    if not min_trump_card:
                        min_trump_card = card
                        self.player_attack = player
                    else:
                        if min_trump_card.rank > card.rank:
                            min_trump_card = card
                            self.player_attack = player
        logger.info(f'Bot start hand: {[card.name for card in self.__players[-1].hand]}')

        if self.player_attack and min_trump_card:
            logger.info(f'Attack player: {self.player_attack.name}, min trump card: {min_trump_card.name}')
        else:
            logger.warning('Players don\'t have trump card!')
            # todo: fix me
            self.player_attack = self.__players[0]
            logger.info(f'Random choice attack player: {self.player_attack.name}')

    def set_trump_card(self):
        self.__trump_card = self.deck.get_card
        if RANK_INDEX_NAME[self.__trump_card.rank] == 'ace':
            logger.warning(f'Ace for trump card: {self.__trump_card.name}')
            self.deck.return_card_in_deck(self.__trump_card)
            # todo: fix me
            self.__trump_card = self.deck.get_card
            logger.warning(f'New trump card: {self.__trump_card.name}')
        logger.info(f'Set trump card: {self.__trump_card.name}')

    @property
    def trump_card(self):
        return self.__trump_card

    def render_trump_card(self):
        self.render.render_image(self.__trump_card.image, POS_TRAMP_CARD)

    def set_client_player(self, player):
        self.__client_player = player

    def client_player(self):
        return self.__client_player

    def add_start_card(self, player):
        for i in range(COUNT_START_CARD):
            card = self.deck.get_card
            player.add_cart(card)
        if player == self.__client_player:
            self.render.draw_pl_cards()
        self.__players.append(player)

    def add_card_in_game_deck(self, card):
        self.__game_deck.add(card)
        card.change_scale(BIG_CARD_WIDTH, BIG_CARD_HEIGHT)
        start_width = GAME_DECK_WIDTH
        for card_in_deck in self.__game_deck:
            card_in_deck.set_position((start_width, GAME_DECK_HEIGHT))
            start_width += 25
        self.__last_card = card
        logger.debug(f'Name: {card.name}, pos: {card.rect}')

    @property
    def game_deck(self):
        return self.__game_deck

    @property
    def len_game_deck(self):
        return len(self.__game_deck)

    @property
    def len_clear_cards(self):
        return len(self.__clear_cards)
