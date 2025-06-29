import json


class Database:
    def load(self):
        try:
            with open("data.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"games": []}
        except json.JSONDecodeError:
            return {"games": []}

    def save(self, data):
        with open("data.json", "w") as f:
            json.dump(data, f)
