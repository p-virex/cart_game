import itertools
from pprint import pprint
from random import choice


class Deck:
    def __init__(self):
        self.colours = ['clubs', 'diamon', 'hearts', 'spades']
        self.count_cart_in_deck = 0
        self.carts = []
        self.cards_value = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
                            'ten': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}
        self.deck = {n + '_of_' + s: v for s in self.colours for n, v in self.cards_value.items()}

    def make_deck(self):
        return

    def get_cart(self):
        return self.deck.get(choice(list(self.deck.keys())))


if __name__ == '__main__':
    deck = Deck()
    pprint(deck.get_cart())
