from menu.base_menu import BaseMenu
from store.games import Games
from store.users import Users

class AdminMenu(BaseMenu):
    def print(self):
        print("Admin Menu:")
        print("a - Add a game")
        print("e - Edit a game")
        print("d - Delete a game")
        print("u - Update a game")
        print("l - List all games")
        print("s - Search for a game")
        print("ua - Add a user")
        print("ue - Edit a user")
        print("ud - Delete a user")
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

    def delete_game(self):
        name = input("Enter the name of the game to delete: ")

        gameManager = Games()
        gameManager.delete(name)

        print(f"Game '{name}' deleted successfully!")

    def save_game_data(self, name, genre, price):
        gameManager = Games()
        gameManager.add(name, genre, price)

        print(f"Game '{name}' added successfully!")

    def add_user(self):
        user_name = input("Enter the name of the user to add: ")
        user_balance = input("Enter the balance of the user (default is 0): ")

        userManager = Users()
        userManager.add(user_name, user_balance)

        print(f"User '{user_name}' added successfully!")

    def edit_user(self):
        name = input("Enter the name of the user to edit: ")
        balance = input("Enter the new balance of the user: ")

        userManager = Users()
        userManager.edit(name, balance)

        print(f"User '{name}' edited successfully!")

    def delete_user(self):
        name = input("Enter the name of the user to delete: ")

        userManager = Users()
        userManager.delete(name)

        print(f"User '{name}' deleted successfully!")