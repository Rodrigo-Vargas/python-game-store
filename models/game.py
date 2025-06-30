from models.entity import Entity


class Game(Entity):
    def __init__(self, id=None, name="", genre="", price=0.0):
        super().__init__()
        self._name = name
        self._genre = genre
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value