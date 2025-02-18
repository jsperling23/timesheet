import os
import json

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


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        items = timeSheet.getSheets(db)
        print(items)
        for item in items:
            print(item)
            if item[3]:
                item[3] = json.loads(item[3])
                print(item[3])
        return render_template("index.j2", items=items)


@app.route('/create', methods=["GET"])
def createSheet():
    timeSheet.createSheet(db)
    return redirect(url_for('home'))


@app.route('/save', methods=["POST"])
def saveSheet():
    sheetID = request.form.get('sheetID')
    rate = request.form.get('rate')
    description = request.form.get('description')
    dates = request.form.getlist('date')
    hours = request.form.getlist('hours')
    lineItems = {}
    for i in range(len(dates)):
        lineItems[i] = {"date": dates[i], "hours": hours[i]}
    lineItems = json.dumps(lineItems)
    print(f'sheetID: {sheetID}\n Rate: {rate}\n Description: {description}\n\
            Line Items: {lineItems}')
    res = timeSheet.saveSheet(db, rate, description, lineItems, sheetID)
    if res:
        print("success")
    else:
        print("error")
    return redirect(url_for('home'))


@app.route('/delete', methods=["GET"])
def deleteSheet():
    sheetID = request.args.get('sheetID')
    print("Delete Imminent, sheet ID: ", sheetID)
    timeSheet.deleteSheet(db, sheetID)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(port=5000, debug=True)
