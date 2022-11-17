from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class Books(FlaskForm):
    book_name = StringField("Book Name", validators=[DataRequired()])
    book_author = StringField("Book Author", validators=[DataRequired()])
    rating = StringField("Rating", validators=[DataRequired()])
    submit = SubmitField("Add Book")


all_books = []


@app.route('/')
def home():
    books = all_books
    return render_template("index.html", books=books)


@app.route("/add", methods=["POST", "GET"])
def add():
    form = Books()
    if form.validate_on_submit():
        book = {
            "title": form.book_name.data,
            "author": form.book_author.data,
            "rating": form.rating.data,
        }
        all_books.append(book)
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
