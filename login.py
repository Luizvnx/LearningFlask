
from flask import Flask, render_template
from config import DevelopmentConfig
from flask import request


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


#Buscar argumentos na URL
@app.get("/")
def get_params():
    searchword = request.args.get('teste')
    return "HELLO"



@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    render_template("login.html")

def show_the_login_form():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
