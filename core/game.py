import pygame

from core.logger import logger
from game.constants import POS_TRAMP_CARD, RANK_INDEX_NAME, COUNT_START_CARD, BIG_CARD_WIDTH, BIG_CARD_HEIGHT, \
    GAME_DECK_WIDTH, GAME_DECK_HEIGHT


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
        self.__player_turn = None

    def game(self):
        if not self.game_deck and self.turn_bot and not self.__player_turn.made_turn:
            # бот делает свой первый ход в кону
            self.first_bot_turn()
        elif self.game_deck and self.turn_bot and self.__client_player.made_turn:
            # если первый ход был сделан, то необходимо проверить, может ли бот добавить карту
            # если может, то добавляет карту, игрок защищается, если нет, то передает ход
            if not self.next_card_from_bot():
                # удаляем метку что бот ходил
                del self.__player_turn.made_turn
                # передаем ход
                self.__player_turn = self.__client_player
                self.clear_game_deck()
        if self.game_deck and not self.turn_bot and self.__player_turn.made_turn:
            # если есть карта в игровой колоде и бот не ходит и игрок походил, то бот защищается
            if not self.defend_bot_card():
                self.pick_up_cards(self.bot)
                del self.__client_player.made_turn
                self.check_cards_in_hands()

    def pick_up_cards(self, player):
        """
        Забрать карты из игровой колоды в руки и взять 1 дополнительную из колоды.
        :param player: игрок который забирает карты
        """
        for card in self.game_deck:
            player.add_cart(card)
        player.add_cart(self.deck.get_card)
        self.__game_deck = pygame.sprite.Group()

    def defend_bot_card(self):
        """
        Защита бота от хода игрока.

        Итерируемся по картам в руке бота и выбираем карту не из козырных которая подходит для защиты.
        Если такой карты нет, берем самую маленькую козырную.
        Если нет то забираем колоду.
        """
        def_card = None
        def_trump_card = None
        for card_in_hand in self.bot.hand:
            if not def_trump_card and card_in_hand.colour == self.trump_card.colour:
                def_trump_card = card_in_hand
                print(def_trump_card)
                continue
            elif def_trump_card and def_trump_card.rank > self.trump_card.rank and card_in_hand.colour == self.trump_card.colour:
                def_trump_card = card_in_hand
                print(def_trump_card)
                continue
            if card_in_hand.colour == self.last_card_in_game_deck.colour and card_in_hand.rank > self.last_card_in_game_deck.rank:
                def_card = card_in_hand
                self.bot_def(def_card)
                print(f'НАШЕЛ НЕ КОЗЫРЬ {def_card.name}')
                break
        if not def_card and def_trump_card:
            def_card = def_trump_card
            self.bot_def(def_trump_card)
        return def_card

    def bot_def(self, card):
        print('!!!!!!!', card.name)
        self.add_card_in_game_deck(card)
        self.bot.remove_card(card)
        self.bot.made_turn = True
        del self.__client_player.made_turn

    def check_cards_in_hands(self):
        for player in self.__players:
            if player.len_hand < 6:
                logger.info(f'Player: {player.name} have {player.len_hand} in hand')
                for i in range(6 - player.len_hand):
                    player.add_cart(self.deck.get_card)

    def clear_game_deck(self):
        """
        Сбросить игровую колоду в отбой
        """
        for card in self.game_deck:
            self.__clear_cards.add(card)
        self.__game_deck = pygame.sprite.Group()
        self.check_cards_in_hands()
        logger.info('Drop game deck')
        print('-'*100)

    def next_card_from_bot(self):
        for card in self.game_deck:
            for card_in_hand in self.__player_turn.hand:
                if card_in_hand.rank == card.rank and card_in_hand.colour != self.trump_card.colour:
                    self.add_card_in_game_deck(card_in_hand)
                    self.__player_turn.remove_card(card_in_hand)
                    self.__last_card = card_in_hand
                    del self.__client_player.made_turn
                    self.__player_turn.made_turn = True
                    print(self.__player_turn.name)
                    return True
        return

    def first_bot_turn(self):
        logger.info(f'Bot move, his cards in hand: {self.__player_turn.cards_in_hand}')
        turn_card = self.__player_turn.bot_first_turn(self.__trump_card)
        self.add_card_in_game_deck(turn_card)
        self.__player_turn.remove_card(turn_card)
        self.__last_card = turn_card
        self.__player_turn.made_turn = True

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
                        self.__player_turn = player
                    else:
                        if min_trump_card.rank > card.rank:
                            min_trump_card = card
                            self.__player_turn = player
        logger.info(f'Bot start hand: {[card.name for card in self.__players[-1].hand]}')

        if self.__player_turn and min_trump_card:
            logger.info(f'Attack player: {self.__player_turn.name}, min trump card: {min_trump_card.name}')
        else:
            logger.warning('Players don\'t have trump card!')
            # todo: fix me
            self.__player_turn = self.__players[-1]
            logger.info(f'Random choice attack player: {self.__player_turn.name}')
        # # todo: DEBUG
        # self.__player_turn = self.__players[-1]

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
        # logger.debug(f'Name: {card.name}, pos: {card.rect}')

    def set_player_turn(self, player):
        self.__player_turn = player

    @property
    def game_deck(self):
        return self.__game_deck

    @property
    def len_game_deck(self):
        return len(self.__game_deck)

    @property
    def len_clear_cards(self):
        return len(self.__clear_cards)

    @property
    def name_turn_player(self):
        return self.__player_turn.name

    @property
    def turn_bot(self):
        if self.name_turn_player == 'Bot':
            return True
        return

    @property
    def bot(self):
        return self.__players[-1]
