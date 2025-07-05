class DatabaseInterface:
    def add_game(self, name, genre, price):
        raise NotImplementedError
    
    def edit_game(self, game):
        raise NotImplementedError
    
    def get_game_by_name(self, game_name):
        raise NotImplementedError
    
    def delete_game(self, game_id):
        raise NotImplementedError
    
    def list_all(self):
        raise NotImplementedError
    
    def get_user_by_name(self, user_name):
        raise NotImplementedError
    
    def edit_user(self, user):
        raise NotImplementedError
    
    def add_user(self, name, balance=0):
        raise NotImplementedError
    
    def delete_user(self, user_name):
        raise NotImplementedError
