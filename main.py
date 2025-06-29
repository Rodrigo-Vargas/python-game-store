import os

from store.database import Database
from store.games import Games

current_user = ""
store_balance = 0.0


def save_game_data(name, genre, price):
    gameManager = Games()
    gameManager.add(name, genre, price)

    print(f"Game '{name}' added successfully!")


def print_welcome_message():
    print("*********************************")
    print("* Welcome to Game Store manager *")
    print("*********************************")
    print("Enter your username")


def print_admin_menu():
    print("Available commands:")
    print("a - Add a game")
    print("d - Delete a game")
    print("l - List all games")
    print("s - Search for a game")
    print("u - Update a game")
    print("q - Quit program")


def add_game():
    game_name = input("Enter the name of the game to add: ")
    game_genre = input("Enter the genre of the game to add: ")
    game_price = input("Enter the price of the game to add: ")

    save_game_data(game_name, game_genre, game_price)

def buy_game():
    game_name = input("Enter the name of the game to buy: ")
    gameManager = Games()
    game = gameManager.get_by_name(game_name)

    if not game:
        print(f"Game '{game_name}' not found.")
        return

    global store_balance

    store_balance += game['price']
    print(f"You have successfully bought '{game_name}' for {game['price']}. Store balance: {store_balance}")

def list_games():
    os.system('clear')
    gameManager = Games()
    games = gameManager.list_all()

    if not games:
        print("No games available.")
        return

    print("Available games:")
    for game in games:
        print(f"Name: {game['name']}, Genre: {game['genre']}, Price: {game['price']}")


def evaluate_user_option():
    option = input("\n")

    if option == "a":
        add_game()

    if option == "b":
        buy_game()

    if option == "l":
        list_games()

    if option == "q":
        return False

    return True


def print_user_menu():
    print("Available commands:")
    print("l - List all games")
    print("s - Search for a game")
    print("b - Buy a game")
    print("q - Quit program")


# os.system('clear')
print_welcome_message()
while True:
    user_name = "user"  # input("")

    sanitized_username = user_name.strip().lower()

    if sanitized_username != "admin" and sanitized_username != "user":
        break

    if sanitized_username == "admin":
        current_user = "admin"

    if current_user == "admin":
        print_admin_menu()
    else:
        print_user_menu()

    if evaluate_user_option() == False:
        break
