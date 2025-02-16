import os

from flask import Flask
from dotenv import load_dotenv

from database import Database
from appConfig import AppConfig


# setup config
load_dotenv()
config = AppConfig(
    **{
        "db_user": os.getenv("DB_USER"),
        "db_password": os.getenv("DB_PASSWORD"),
        "db_name": os.getenv("DB_NAME"),
        "db_host": os.getenv("DB_HOST"),
        "secret_key": os.getenv("SECRET_KEY"),
    }
)

# setup flask server and database
app = Flask(__name__)
app.secret_key = config.secret_key
db = Database(config)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
