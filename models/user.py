from sqlalchemy.orm import mapped_column
from models.base import Base
from sqlalchemy import Integer, String, Text, DateTime, func
import bcrypt
from flask_login import UserMixin


class User(Base, UserMixin):
    __tablename__ = 'user_data_login'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String(50), nullable=False)
    email = mapped_column(String(100), nullable=False)
    password = mapped_column(String(190), nullable=False)
    created_at = mapped_column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, created_at={self.created_at})>"
    
    def set_password(self, password):
        self.password = bcrypt.hashpw( password.encode('utf-8') , bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
