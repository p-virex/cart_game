class Player:
    def __init__(self):
        self.__arm = list()

    @property
    def arm(self):
        return self.__arm

    def add_cart(self, card):
        self.__arm.append(card)

    def remove_card(self, pos):
        return self.__arm.pop(pos)

    @property
    def len_arm(self):
        return len(self.arm)
