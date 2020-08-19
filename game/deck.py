import itertools
from pprint import pprint
from random import shuffle

from game.card import Card
from game.constants import COLOUR_INDEX, RANK_INDEX


class Deck:
    def __init__(self):
        self.__card_deck = list()

    def make_deck(self):
        for color in COLOUR_INDEX:
            for rank in RANK_INDEX:
                self.__card_deck.append(Card(color, rank))

    def shuffle_deck(self):
        shuffle(self.__card_deck)

    @property
    def get_deck(self):
        return self.__card_deck

    @property
    def get_cart(self):
        return self.__card_deck.pop()

    @property
    def get_len_deck(self):
        return len(self.__card_deck)


if __name__ == '__main__':
    deck = Deck()
    deck.make_deck()
    deck.shuffle_deck()
    card = deck.get_cart
    print(card.get_name, card.get_colour, card.get_rank)
    print(deck.get_len_deck)

    # for card in deck.get_deck:
    #     print(card.get_name)
