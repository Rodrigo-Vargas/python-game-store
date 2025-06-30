import os

from store.games import Games

class BaseMenu():
    def list_games(self):
        os.system('clear')
        gameManager = Games()
        games = gameManager.list_all()

        if not games:
            print("No games available.")
            return

        print("Available games:")
        for game in games:
            print(f"Name: {game['name']}, Genre: {game['genre']}, Price: {game['price']}")
