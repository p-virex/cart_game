from pprint import pprint

SIZE_WINDOW = (1200, 800)

FPS_WINDOW = 60

COLOUR_INDEX = [x for x in range(0, 4)]

RANK_INDEX = [x for x in range(1, 14)]

COLOUR_NAME = ['clubs', 'diamonds', 'hearts', 'spades']

COLOUR_NAME_INDEX = {COLOUR_NAME[i]: i for i in COLOUR_INDEX}
COLOUR_INDEX_NAME = {i: COLOUR_NAME[i] for i in COLOUR_INDEX}

RANK_NAME = [
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'jack',
    'queen',
    'king',
    'ace'
]


RANK_NAME_INDEX = {RANK_NAME[i - 1]: i for i in RANK_INDEX}
RANK_INDEX_NAME = {i: RANK_NAME[i - 1] for i in RANK_INDEX}
