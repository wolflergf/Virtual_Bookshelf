from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///all_books.db"
# initialize the app with the extension
db.init_app(app)

all_books = []


@app.route('/')
def home():
    pass


@app.route("/add")
def add():
    pass


if __name__ == "__main__":
    app.run(debug=True)

