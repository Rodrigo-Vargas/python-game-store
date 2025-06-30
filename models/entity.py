class Entity:
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value