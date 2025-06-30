from menu.base_menu import BaseMenu

class UserMenu(BaseMenu):
    def print(self):
        print("Available commands:")
        print("l - List all games")
        print("s - Search for a game")
        print("b - Buy a game")
        print("q - Quit program")