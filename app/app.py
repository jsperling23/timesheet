import os

from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

from database import Database
from appConfig import AppConfig
from timeSheet import TimeSheet


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

timeSheet = TimeSheet()


# routes
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        items = timeSheet.getSheets(db, 1)
        return render_template("index.j2", items=items, userID=1)


@app.route('/create', methods=["GET"])
def createSheet():
    userID = request.args.get('userID')
    timeSheet.createSheet(db, userID)
    return redirect(url_for('home'))

@app.route('/update', methods=["POST"])
def createSheet():
    userID = request.args.get('userID')
    timeSheet.createSheet(db, userID)
    return redirect(url_for('home'))
if __name__ == "__main__":
    app.run(port=5000, debug=True)
