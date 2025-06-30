from store.database import Database
import uuid

class Games:
    def add(self, name, genre, price):
        database = Database()
        data = database.load()

        print(data)

        data["products"].append({
            "id": str(uuid.uuid4()),
            "name": name,
            "genre": genre,
            "price": float(price)
        })

        database.save(data)

    def edit(self, name, genre, price):
        database = Database()
        data = database.load()

        for game in data["products"]:
            if game["name"].lower() == name.lower():
                game["genre"] = genre
                game["price"] = float(price)
                break
        
        database.save(data)

    def delete(self, name):
        database = Database()
        data = database.load()

        data["products"] = [game for game in data["products"] if game["name"].lower() != name.lower()]

        database.save(data)

    def list_all(self):
        database = Database()
        data = database.load()

        return data["products"]
    
    def buy(self, name, current_user):
        database = Database()
        data = database.load()

        game_id = ""

        for game in data["products"]:
            if game["name"].lower() == name.lower():
                game_id = game["id"]
                break
        
        if game_id != "":
            for user in data["users"]:
                if user["name"].lower() == current_user.lower():
                    user["games"].append(game_id)

                    user["balance"] -= game["price"]
                    break
            database.save(data)

        return False

    def get_by_name(self, name):
        database = Database()
        data = database.load()

        for game in data["products"]:
            if game["name"].lower() == name.lower():
                return game

        return None