from menu.base_menu import BaseMenu
from store.games import Games

class AdminMenu(BaseMenu):
    def print(self):
        print("Admin Menu:")
        print("a - Add a game")
        print("e - Edit a game")
        print("d - Delete a game")
        print("u - Update a game")
        print("l - List all games")
        print("s - Search for a game")
        print("q - Quit program")

    def add_game(self):
        game_name = input("Enter the name of the game to add: ")
        game_genre = input("Enter the genre of the game to add: ")
        game_price = input("Enter the price of the game to add: ")

        self.save_game_data(game_name, game_genre, game_price)

    def edit_game(self):
        name = input("Enter the name of the game to edit: ")
        genre = input("Enter the new genre of the game: ")
        price = input("Enter the new price of the game: ")

        gameManager = Games()
        gameManager.edit(name, genre, price)
        
        print(f"Game '{name}' edited successfully!")

    def save_game_data(self, name, genre, price):
        gameManager = Games()
        gameManager.add(name, genre, price)

        print(f"Game '{name}' added successfully!")