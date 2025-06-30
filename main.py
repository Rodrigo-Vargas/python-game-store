import os

from menu.admin_menu import AdminMenu
from menu.user_menu import UserMenu
from store.games import Games

current_user = ""
store_balance = 0.0
menu = None


def print_welcome_message():
    print("*********************************")
    print("* Welcome to Game Store manager *")
    print("*********************************")
    print("Enter your username")


def buy_game():
    game_name = input("Enter the name of the game to buy: ")
    gameManager = Games()
    game = gameManager.get_by_name(game_name)

    if not game:
        print(f"Game '{game_name}' not found.")
        return
    
    gameManager.buy(game_name, current_user)

    global store_balance

    store_balance += game.price
    print(f"You have successfully bought '{game_name}' for {game.price}. Store balance: {store_balance}")


def evaluate_user_option():
    option = input("\n")

    if option == "q":
        print("Exiting the program. Goodbye!")
        return False

    if option == "a":
        menu.add_game()

    if option == "b":
        buy_game()

    if option == "d":
        menu.delete_game()

    if option == "e":
        menu.edit_game()

    if option == "l":
        menu.list_games()

    if option == "ua":
        menu.add_user()

    if option == "ue":
        menu.edit_user()
    
    if option == "ud":
        menu.delete_user()

    return True

# os.system('clear')
print_welcome_message()
while True:
    user_name = "admin"  # input("")

    sanitized_username = user_name.strip().lower()

    if sanitized_username != "admin" and sanitized_username != "user":
        break

    current_user = sanitized_username

    
    if current_user == "admin":
        menu = AdminMenu()
    else:
        menu = UserMenu()

    menu.print()

    if evaluate_user_option() == False:
        break
