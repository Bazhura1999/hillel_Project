from sqlalchemy import Column, Integer, String, REAL
from al_db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(50))
    password = Column(String(120))
    email = Column(String(120))
    first_name = Column(String(50))
    surname = Column(String(50))

    def __init__(self, username, password, email=None, first_name=None, surname=None):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.surname = surname

    def __repr__(self):
        return f'<User{self.username!r}>'