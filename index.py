from flask import Flask
from dotenv import load_dotenv
from models.user import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from connectors.mysql_connectors import connection
from controllers.user import user_routes
from flask_cors import CORS
from flask_login import LoginManager
import os



load_dotenv()
app=Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

login_manager = LoginManager()
login_manager.init_app(app)
CORS(app)
app.register_blueprint(user_routes)


# @app.route("/")
# def user_db():
#     user_query = select(User)
#     Session = sessionmaker(connection)
#     with Session() as session:
#         result = session.execute(user_query)
#         for row in result.scalars():
#             print(f'ID: {row.id}, Name: {row.username}')
    
#     return "<p>Insert Success</p>"
