from flask import Flask, render_template
from markupsafe import escape
from config import DevelopmentConfig
from flask import url_for
from flask import request


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route("/")
def hello_world():
    message = "Hello, World!"
    #return render_template("index.html", message=message)
    return message

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


@app.route("/about")
def about():
    return "<p>About Page</p>"


with app.test_request_context():
    print(url_for('profile', username = 'John'))
    print(url_for('hello', name='John'))


if __name__ == "__main__":
    app.run()
