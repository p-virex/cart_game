# здесь подключаются модули
from pprint import pprint

import pygame

# здесь определяются константы, классы и функции
from core.render import RenderCard
from game.deck import Deck

FPS = 60

# здесь происходит инициация, создание объектов и др.
pygame.init()
pygame.display.set_caption('Card game')
screen = pygame.display.set_mode((1200, 800))
screen.fill((42, 113, 0))
clock = pygame.time.Clock()

# если надо до цикла отобразить объекты на экране
pygame.display.update()

render_card = RenderCard(screen)

deck = Deck()
deck.make_deck()
deck.shuffle_deck()
card = deck.get_cart

card_2 = deck.get_cart
# render_card.render('2_of_clubs', (156, 275))
# главный цикл
x, y = 100, 100
while True:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

            render_card.render_image(i, (x, y))
            print(x, y)
    # --------
    # изменение объектов и многое др.
    # --------

    # render_card.render_image(i, (150, 250))
    i_2 = render_card.change_scale(card_2.image, 5)
    render_card.render_image(i_2, (105,  145))
    # обновление экрана
    pygame.display.update()
