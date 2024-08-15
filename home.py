from flask import Flask, render_template
from flask import request
from config import DevelopmentConfig
import pywhatkit
import pywhatkit.whats
import logging

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.get("/")
def home():
    return render_template("home.html")

@app.route("/enviar_mensagem", methods=["GET", "POST"])
def enviar_mensagem():
    try:
        if request.method == "GET":
            return render_template("enviar_mensagem.html")
        elif request.method == "POST":
            phone = request.form.get("phone", default=None)
            msg = request.form.get("message", default=None)
            hour = int(request.form.get("hour", default=None))
            minute = int(request.form.get("minute", default=None))

            if not all([phone, msg, hour, minute]):
                return "Invalid input", 400

            pywhatkit.whats.sendwhatmsg(phone, msg, hour, minute)
            return "Mensagem enviada"
    except Exception as e:
        logging.error(e)
        return "Error sending message", 500

if __name__ == "__main__":
    app.run()
