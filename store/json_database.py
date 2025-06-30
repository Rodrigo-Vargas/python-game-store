import json
import uuid

from models.game import Game
from models.user import User
from .database_interface import DatabaseInterface

class JsonDatabase(DatabaseInterface):
    def _load(self):
        try:
            with open("data.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"products": [], "users": []}
        except json.JSONDecodeError:
            return {"products": [], "users": []}

    def _save(self, data):
        with open("data.json", "w") as f:
            json.dump(data, f)

    def add_game(self, name, genre, price):
        data = self._load()
        new_game = {
            "id": str(uuid.uuid4()),
            "name": name,
            "genre": genre,
            "price": float(price)
        }
        data["products"].append(new_game)
        self._save(data)

    def edit_game(self, game: Game):
        print(f"Editing game: {game.name} with ID: {game.id}")
        data = self._load()
        for existing_game in data["products"]:
            if existing_game["id"] == game.id:
                existing_game["genre"] = game.genre
                existing_game["price"] = float(game.price)
                break
        self._save(data)

    def get_game_by_name(self, name):
        data = self._load()
        for game in data["products"]:
            if game["name"] == name:
                gameModel = Game()
                gameModel.id = game["id"]
                gameModel.name = game["name"]
                gameModel.genre = game["genre"]
                gameModel.price = game["price"]
                return gameModel
        return None
    
    def delete_game(self, game_id):
        data = self._load()
        data["products"] = [game for game in data["products"] if game["id"] != game_id]
        self._save(data)

    def list_all(self):
        data = self._load()
        return data["products"]
    
    def get_user_by_name(self, user_name):
        data = self._load()
        for user in data["users"]:
            if user["name"].lower() == user_name.lower():
                userModel = User()
                userModel.id = user["id"]
                userModel.name = user["name"]
                userModel.balance = float(user["balance"])
                userModel.games = user["games"]
                return userModel
        return None
    
    def edit_user(self, user):
        data = self._load()
        for existing_user in data["users"]:
            if existing_user["name"].lower() == user.name.lower():
                existing_user["balance"] = float(user.balance)
                existing_user["games"] = user.games
                break
        self._save(data)