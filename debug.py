class Mine(object):

    def __init__(self):
        self._x = None

    x = property()

    @x.getter
    def x(self):
        """Это свойство x."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        self._x = 'No more'