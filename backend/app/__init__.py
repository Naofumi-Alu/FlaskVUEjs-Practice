from flask import Flask
from .routes.Routes import Routes_bp


#INSTANTIATE THE APP

def create_app():
    app = Flask(__name__)
    app.register_blueprint(Routes_bp)
    return app