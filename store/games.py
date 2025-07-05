from models.game import Game

from store.database_factory import DatabaseFactory

class Games:
    def __init__(self):
        self.database = DatabaseFactory.get_database()

    def add(self, name, genre, price):
        self.database.add_game(name, genre, price)

    def edit(self, name, genre, price):        
        existent_game = self.database.get_game_by_name(name)
        
        game = Game()
        game.id = existent_game.id
        game.name = name
        game.genre = genre
        game.price = float(price)

        self.database.edit_game(game)

    def delete(self, name):
        game = self.database.get_game_by_name(name)
        self.database.delete(game.id)

    def list_all(self):
        return self.database.list_all()
    
    def buy(self, name, current_user):
        game = self.database.get_game_by_name(name)
        
        if game.id != "":
            user = self.database.get_user_by_name(current_user.lower())
            user.balance -= game.price
            self.database.edit_user(user)
            
            return True

        return False

    def get_by_name(self, name):
        return self.database.get_game_by_name(name)