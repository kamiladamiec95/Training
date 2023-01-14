from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

class NamerForm(FlaskForm):
    name = StringField("Whats your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/')
def index():
    favourite_pizza = ["Pepperoni", "Margarita"]
    return render_template("index.html",favourite_pizza=favourite_pizza)


@app.route('/user/<name>')
def user(name):
    first_name = "test"
    return render_template("user.html", user_name=name, first_name=first_name)   



@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('name.html', name=name, form=form)