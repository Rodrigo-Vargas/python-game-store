import configparser
from .json_database import JsonDatabase
from .sqlite_database import SqliteDatabase

class DatabaseFactory:
    @staticmethod
    def get_database():
        config = configparser.ConfigParser()
        config.read('config.ini')

        db_type = config['database']['type']

        if db_type == "sqlite":
            return SqliteDatabase()
        return JsonDatabase()
