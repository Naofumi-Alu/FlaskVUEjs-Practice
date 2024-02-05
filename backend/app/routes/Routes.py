# backend/routes/Routes.py
from flask import Blueprint
from markupsafe import escape
# Crete a blueprint  Routes

Routes_bp = Blueprint('routes',__name__)

def hola_mundo(name="Caro"):
    return f"<p>Hello , {escape(name)}! welcome to the world</p>"


def hola_mundo_Default():
    return f"<p>Hello Caro i love you</p>"

@Routes_bp.route("/")
def saludo ():
    return f"<p>Hello world !</p>"


@Routes_bp.route("/Saludo")
def saludo_basico():
    return hola_mundo_Default()



@Routes_bp.route("/Saludo/<name>")
def saludo_personalizado(name):
    return hola_mundo(name)


