from flask import Flask
from dotenv import load_dotenv
from models.user import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from connectors.mysql_connectors import connection
from controllers.user import user_routes
from connectors.mysql_connectors import engine

from flask_login import LoginManager
import os



load_dotenv()
app=Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return "ASd"
app.register_blueprint(user_routes)

