DEBUG = True
SHORT_DECK = True

FPS = 60

SIZE_WINDOW = WIDTH, HEIGHT = (1200, 800)

WHITE = (255, 255, 255)

FPS_WINDOW = 60

GREEN_TABLE = (42, 113, 0)

COLOUR_INDEX = [x for x in range(0, 4)]

RANK_INDEX = [x for x in range(1, 14 if not SHORT_DECK else 10)]

COLOUR_NAME = ['clubs', 'diamonds', 'hearts', 'spades']

COLOUR_NAME_INDEX = {COLOUR_NAME[i]: i for i in COLOUR_INDEX}
COLOUR_INDEX_NAME = {i: COLOUR_NAME[i] for i in COLOUR_INDEX}

LONG_DECK_RANK_NAME = [
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

SHORT_DECK_RANK_NAME = ['6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

RANK_NAME = LONG_DECK_RANK_NAME if not SHORT_DECK else SHORT_DECK_RANK_NAME

RANK_NAME_INDEX = {RANK_NAME[i - 1]: i for i in RANK_INDEX}
RANK_INDEX_NAME = {i: RANK_NAME[i - 1] for i in RANK_INDEX}

START_POS_PLAYER_ARM = (5, 645)
POS_TRAMP_CARD = (105, 400)
COUNT_START_CARD = 6
MAX_COUNT_CARD_IN_ARM = 25

BASE_CARD_WIDTH, BASE_CARD_HEIGHT = 100, 150
BIG_CARD_WIDTH, BIG_CARD_HEIGHT = 150, 200

POS_GAME_DECK = GAME_DECK_WIDTH, GAME_DECK_HEIGHT = (WIDTH/2-BIG_CARD_WIDTH/2, HEIGHT/2-BIG_CARD_HEIGHT/2)

WIDTH_CARD_FOR_UI = BASE_CARD_WIDTH + 5

ZONE_FOR_CARDS = WIDTH_CARD_FOR_UI * 6
MAX_ZONE_FOR_CARDS = WIDTH_CARD_FOR_UI * 10
