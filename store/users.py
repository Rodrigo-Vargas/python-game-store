from store.database import Database

class Users:
    def add(self, name, balance=0):
        database = Database()
        data = database.load()

        if (balance is None or balance == ""):
            balance = 0

        data["users"].append({
            "name": name,
            "balance": float(balance),
            "games": []
        })

        database.save(data)

    def edit(self, name, balance):
        database = Database()
        data = database.load()

        for user in data["users"]:
            if user["name"].lower() == name.lower():
                user["balance"] = float(balance)
                break
        
        database.save(data)

    def delete(self, name):
        database = Database()
        data = database.load()

        data["users"] = [user for user in data["users"] if user["name"].lower() != name.lower()]

        database.save(data)