class Entity:
    def __init__(self, id=""):
        self.id = id

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value