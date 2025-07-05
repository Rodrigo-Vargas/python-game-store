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

        self._print_header()
        for game in games:
            self._print_game_row(
                game.id,
                game.name,
                game.price,
                game.genre
            )

    def _print_header(self):
        print("ID   Name            Price   Genre")
        print("--   --------------  ------- ------------- ")

    def _print_game_row(self, id, name, price, genre):
        print(f"{id:<4} {name:<15} {price:<7} {genre:<9}")
        