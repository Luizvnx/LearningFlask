from flask import Flask, render_template
from flask import request
from config import DevelopmentConfig
import usecases.enviar_mensagem

app = Flask(__name__)
#app.config.from_object(DevelopmentConfig)
uc = usecases

@app.get("/")
def home():
    return render_template("home.html")

@app.route("/enviar_mensagem", methods=["GET", "POST"])
def enviar_mensagem():
    try:
        if request.method == "GET":
            return render_template("enviar_mensagem.html")
        
        uc.enviar_mensagem.enviar_mensagem_impl()
        return "Mensagem enviada"

    except Exception as e:
        return e

if __name__ == "__main__":
    app.run()
