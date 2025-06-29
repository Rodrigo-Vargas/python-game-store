from store.database import Database


class Games:
    def add(self, name, genre, price):
        database = Database()
        data = database.load

        data.products.append({"name": name, "genre": genre, "price": float(price)})

        database.save(data)

    def list_all(self):
        database = Database()
        data = database.load()

        return data["products"]

    def get_by_name(self, name):
        database = Database()
        data = database.load()

        for game in data["products"]:
            if game["name"].lower() == name.lower():
                return game

        return None