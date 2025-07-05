from store.database_factory import DatabaseFactory


class Users:
    def __init__(self):
        self.database = DatabaseFactory.get_database()

    def add(self, name, balance=0):
        self.database.add_user(name, balance)

    def edit(self, name, balance):
        self.database.edit_user(name, balance)

    def delete(self, name):
        self.database.delete_user(name)