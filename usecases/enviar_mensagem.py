from flask import Flask, request, render_template
from config import DevelopmentConfig
import pywhatkit
import pywhatkit.whats
import logging


def enviar_mensagem_impl():
    try:
        phone = request.form.get("phone", default=None)
        msg = request.form.get("message", default=None)
        hour = int(request.form.get("hour", default=None))
        minute = int(request.form.get("minute", default=None))

        if not all([phone, msg, hour, minute]):
            return "Invalid input", 400

        pywhatkit.whats.sendwhatmsg(phone, msg, hour, minute)

    
    except Exception as e:
        logging.error(e)
        return "Error sending message", 500
    
