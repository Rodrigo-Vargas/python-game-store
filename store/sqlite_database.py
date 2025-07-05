import sqlite3
import uuid

from models.game import Game
from models.user import User
from .database_interface import DatabaseInterface

class SqliteDatabase(DatabaseInterface):
    def __init__(self, db_path="data.db"):
        self.db_path = db_path
        self._ensure_tables()

    def _ensure_tables(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS products (
            id TEXT PRIMARY KEY,
            name TEXT,
            genre TEXT,
            price REAL
        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            name TEXT PRIMARY KEY,
            balance REAL,
            games TEXT
        )''')
        conn.commit()
        conn.close()

    def add_game(self, name, genre, price):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        game_id = str(uuid.uuid4())
        cursor.execute('INSERT INTO products (id, name, genre, price) VALUES (?, ?, ?, ?)',
                       (game_id, name, genre, float(price)))
        conn.commit()
        conn.close()

    def edit_game(self, game):
        print(f"Editing game: {game.name} with ID: {game.id}")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('UPDATE products SET name = ?, genre = ?, price = ? WHERE id = ?',
                       (game.name, game.genre, float(game.price), game.id))
        conn.commit()
        conn.close()

    def get_game_by_name(self, name):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products WHERE name = ?', (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            gameModel = Game()
            gameModel.id = row[0]
            gameModel.name = row[1]
            gameModel.genre = row[2]
            gameModel.price = row[3]
            return gameModel
        return None
    
    def delete_game(self, game_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM products WHERE id = ?', (game_id,))
        conn.commit()
        conn.close()

    def list_all(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        rows = cursor.fetchall()
        conn.close()
        return [Game(id=row[0], name=row[1], genre=row[2], price=row[3]) for row in rows]
    
    def get_user_by_name(self, user_name):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE name = ?', (user_name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            userModel = User()
            userModel.name = row[0]
            userModel.balance = row[1]
            userModel.games = row[2]
            return userModel
        return None
    
    def edit_user(self, user):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET balance = ?, games = ? WHERE name = ?',
                       (float(user.balance), user.games, user.name))
        conn.commit()
        conn.close()

    def add_user(self, name, balance=0):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, balance, games) VALUES (?, ?, ?)',
                       (name, float(balance), "[]"))
        conn.commit()
        conn.close()

    def delete_user(self, user_name):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE name = ?', (user_name,))
        conn.commit()
        conn.close()
