
from flask import Flask, render_template
from flask import request
from config import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


#Buscar argumentos na URL
#@app.get("/")
#def get_params():
#    searchword = request.args.get('teste')
#    return "HELLO"


@app.get("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run()
